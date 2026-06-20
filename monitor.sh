#!/bin/bash

echo "Linux Self-Healing Monitor Started"

DATE=$(date)

echo "Current Time: $DATE"

echo "--------------------"

CPU=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}')

echo "CPU Usage: $CPU %"

MEMORY=$(free -m | awk 'NR==2{printf"%.2f", $3*100/$2}')

echo "Memory Usage: $MEMORY %"

MEMORY_INT=$(printf "%.0f" "$MEMORY")

if [ "$MEMORY_INT" -gt 80 ]
then
    echo "WARNING: Memory Usage Above 80%"
    echo "$(date) - Memory Usage Above 80%" >> incident.log
fi

DISK=$(df -h / | awk 'NR==2 {print $5}')

echo "Disk Usage: $DISK"

DISK_PERCENT=$(df -h / | awk 'NR==2 {gsub("%","",$5); print $5}')

if [ "$DISK_PERCENT" -gt 80 ]
then
    echo "WARNING: Disk Usage Above 80%"
    echo "$(date) - Disk Usage Above 80%" >> incident.log
fi

SERVICE="cron"

if systemctl is-active --quiet $SERVICE
then
    echo "$SERVICE Service: Running"
else
    echo "$SERVICE Service: Down"
    echo "Attempting restart. . ."

    sudo systemctl restart $SERVICE

    echo "$(date) - $SERVICE was down and restarted" >> incident.log

    echo "$SERVICE restarted successfully"
fi

echo "$(date) - Health Check Completed" >> monitor.log  
