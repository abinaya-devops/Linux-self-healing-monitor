🚀 Linux Self-Healing Monitor

A complete DevOps Monitoring & Self-Healing System built using Linux, Bash, Python Flask, Docker, HTML, CSS, Git and GitHub.

This project continuously monitors system resources, automatically recovers failed services, sends email alerts, and provides a beautiful real-time monitoring dashboard.

---

✨ Features

📊 Real-Time Monitoring Dashboard

- Real-Time CPU Usage Monitoring
- Real-Time Memory Usage Monitoring
- Real-Time Disk Usage Monitoring
- Live Health Score
- Live Service Status
- Last Updated Timestamp
- Auto Refresh Dashboard

---

🖥️ System Information

Displays

- Hostname
- Operating System
- System Uptime

---

📈 Performance History

Stores and displays

- CPU History
- Memory History
- Disk Usage History
- Health Score History

using interactive charts.

---

🔄 Self-Healing

Automatically

- Detects service failure
- Restarts failed service
- Logs recovery action

---

🚨 Incident Management

- Incident Logging
- Recent Events Timeline
- Download Incident Log

---

📧 Email Alerts

Automatically sends email notifications whenever

- Service goes DOWN
- Auto-Healing starts
- Service recovery occurs

---

🐳 Docker Support

Project runs inside Docker Container.

Dashboard automatically detects container execution and displays:

Service Status → Container Mode

---

🛠 Technologies Used

- Linux (Ubuntu)
- Bash Scripting
- Python
- Flask
- HTML5
- CSS3
- Docker
- Git
- GitHub

---

📂 Project Structure

linux-self-healing-monitor/

├── app.py
├── monitor.sh
├── send_email.py
├── Dockerfile
├── requirements.txt
├── incident.log
├── cpu_history.log
├── memory_history.log
├── disk_history.log
├── health_history.log
├── templates/
│ └── index.html
├── static/
│ └── style.css
├── screenshots/
└── README.md

---

▶ Running the Project

Clone Repository

git clone <repository-url>
cd linux-self-healing-monitor

---

Create Virtual Environment

python3 -m venv venv
source venv/bin/activate

---

Install Dependencies

pip install -r requirements.txt

---

Start Dashboard

python app.py

Open

http://localhost:5000

---

🐳 Run with Docker

Build Docker Image

docker build -t linux-self-healing-monitor .

Run Docker Container

docker run -d -p 5000:5000 --name self-healing-monitor linux-self-healing-monitor

Open

http://localhost:5000

---

📸 Screenshots

Project screenshots are available inside the screenshots/ folder.

---

🚀 Future Improvements

- Telegram Notifications
- Slack Notifications
- Microsoft Teams Alerts
- Prometheus Integration
- Grafana Dashboard
- Kubernetes Deployment
- AWS CloudWatch Integration
- Multi-Service Monitoring

---

👩‍💻 Author

Abinaya M

Aspiring DevOps Engineer | Cloud Computing Enthusiast

