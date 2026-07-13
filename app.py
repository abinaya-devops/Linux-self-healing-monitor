from flask import Flask, render_template, jsonify, send_file
from datetime import datetime
import subprocess

app = Flask(__name__)

def get_incidents():

    try:
        with open("incident.log", "r") as file:

            lines = file.readlines()

            return lines[-5:][::-1]

    except:
        return ["No incidents found"]

def get_cpu_history():

    try:
        with open("cpu_history.log", "r") as file:

            lines = file.readlines()

            history = [float(line.strip()) for line in lines[-10:]]

            return history

    except:
        return [0]

def get_memory_history():

    try:
        with open("memory_history.log", "r") as file:

            lines = file.readlines()

            history = [float(line.strip()) for line in lines[-10:]]

            return history

    except:
        return [0]

def get_disk_history():

    try:
        with open("disk_history.log", "r") as file:

            lines = file.readlines()

            history = [float(line.strip()) for line in lines[-10:]]

            return history

    except:
        return [0]

def get_health_history():

    try:
        with open("health_history.log", "r") as file:

            lines = file.readlines()

            history = [int(line.strip()) for line in lines[-10:]]

            return history

    except:
        return [100]

def get_system_data():

    cpu = subprocess.getoutput(
        "top -bn1 | grep 'Cpu(s)' | awk '{print $2}'"
    )

    memory = subprocess.getoutput(
        "free -m | awk 'NR==2{printf \"%.0f%%\", $3*100/$2 }'"
    )

    disk = subprocess.getoutput(
        "df -h / | awk 'NR==2 {print $5}'"
    )

    service_check = subprocess.getoutput("which systemctl")

    if service_check:
        service = subprocess.getoutput(
        "systemctl is-active cron")
        docker_mode = False
    else:
        service = "Container Mode"
        docker_mode = True
    
    memory_value = int(memory.replace("%", ""))
    disk_value = int(disk.replace("%", ""))

    health_score = 100

    if memory_value > 80:
        health_score -= 10

    if disk_value > 80:
        health_score -= 10

    if not docker_mode and service != "active":
        health_score -= 40

    if health_score >= 80:
        status = "Healthy"
        status_class = "healthy"

    elif health_score >= 50:
        status = "Warning"
        status_class = "warning"

    else:
        status = "Critical"
        status_class = "critical"

    hostname = subprocess.getoutput("hostname")

    uptime = subprocess.getoutput("uptime -p")

    os_name = subprocess.getoutput("grep PRETTY_NAME /etc/os-release | cut -d= -f2 | tr -d '\"'")

    return {
        "cpu": cpu + "%",
        "memory": memory,
        "disk": disk,
        "service": service.capitalize(),
        "health": str(health_score) +"%",
        "status": status,
        "status_class": status_class,
        "hostname": hostname,
        "uptime": uptime,
        "os_name": os_name
    }

@app.route("/")
def home():

    system_data = get_system_data()
    cpu_history = get_cpu_history()
    memory_history = get_memory_history()
    disk_history = get_disk_history()
    health_history = get_health_history()

    data = {
        "cpu": system_data["cpu"],
        "memory": system_data["memory"],
        "disk": system_data["disk"],
        "service": system_data["service"],
        "health": system_data["health"],
        "status": system_data["status"],
        "status_class": system_data["status_class"],
        "updated": datetime.now().strftime("%d %b %Y %H:%M:%S"),
        "hostname": system_data["hostname"],
        "uptime": system_data["uptime"],
        "os_name": system_data["os_name"]
    }

    events = get_incidents()

    return render_template(
        "index.html",
        data=data,
        events=events,
        cpu_history=cpu_history,
        memory_history=memory_history,
        disk_history=disk_history,
        health_history=health_history
    )

@app.route("/api/data")
def api_data():

    system_data = get_system_data()

    return jsonify({
        "cpu": system_data["cpu"],
        "memory": system_data["memory"],
        "disk": system_data["disk"],
        "service": system_data["service"],
        "health": system_data["health"],
        "incidents": get_incidents(),
        "memory_history": get_memory_history()
    })
@app.route("/download-log")
def download_log():

    return send_file(
        "incident.log",
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
