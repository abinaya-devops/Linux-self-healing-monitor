#!/bin/bash

MEMORY_THRESHOLD=80
DISK_THRESHOLD=80

echo "Linux Self-Healing Monitor Started"

DATE=$(date)

echo "Current Time: $DATE"

touch incident.log

echo "--------------------"

CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}')

echo "CPU Usage: $CPU %"

echo "$CPU" >> cpu_history.log

MEMORY=$(free -m | awk 'NR==2{printf"%.2f", $3*100/$2}')

echo "Memory Usage: $MEMORY %"

echo "$MEMORY" >> memory_history.log

MEMORY_INT=$(printf "%.0f" "$MEMORY")

if [ "$MEMORY_INT" -gt "$MEMORY_THRESHOLD" ]
then
    echo "WARNING: Memory Usage Above 80%"
    echo "$(date) - Memory Usage Above 80%" >> incident.log
fi

DISK=$(df -h / | awk 'NR==2 {print $5}')

echo "Disk Usage: $DISK"

DISK_PERCENT=$(df -h / | awk 'NR==2 {gsub("%","",$5); print $5}')

echo "$DISK_PERCENT" >> disk_history.log

DISK_PERCENT=$(df -h / | awk 'NR==2 {gsub("%","",$5); print $5}')

if [ "$DISK_PERCENT" -gt "$DISK_THRESHOLD" ]
then
    echo "WARNING: Disk Usage Above 80%"
    echo "$(date) - Disk Usage Above 80%" >> incident.log
fi

HEALTH_SCORE=100

if [ "$MEMORY_INT" -gt 80 ]
then
    HEALTH_SCORE=$((HEALTH_SCORE-10))
fi

if [ "$DISK_PERCENT" -gt 80 ]
then
    HEALTH_SCORE=$((HEALTH_SCORE-10))
fi

EMAIL="abinaya12.tech@gmail.com"

APP_PASSWORD="zwqd qhrv vyvx wrxn"

SUBJECT="Linux Self-Healing Monitor Alert"

BODY="The cron service was down and has been restarted automatically."

SERVICE="cron"

if systemctl is-active --quiet $SERVICE
then
    echo "$SERVICE Service: Running"
    echo "Health Score: $HEALTH_SCORE%"
else
    echo "$SERVICE Service: Down"
    HEALTH_SCORE=$((HEALTH_SCORE-40))
    echo "Attempting restart. . ."

    sudo systemctl restart $SERVICE

    sleep 2

    if systemctl is-active --quiet $SERVICE
    then
        echo "$SERVICE restarted successfully"
        echo "$(date) - $SERVICE restarted successfully" >> incident.log
        python3 send_email.py
    else
        echo "CRITICAL: $SERVICE failed to restart"
        echo "$(date) - CRITICAL: $SERVICE failed to restart" >> incident.log
    fi
fi

echo "$(date) - Health Check Completed" >> monitor.log

echo "$HEALTH_SCORE" >> health_history.log
echo "Health Check Status: OK"
