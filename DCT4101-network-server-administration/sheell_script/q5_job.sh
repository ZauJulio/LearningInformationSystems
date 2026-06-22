#!/bin/bash

# Check if /home/$USER/savedate exists
if [ ! -d /home/$USER/savedate ]; then
    # If exist log date, hour and system load on /home/$USER/logdate.txt
    echo "Date: $(date +%d/%m/%Y) Hour: $(date +%H:%M:%S) Load: $(uptime | awk '{print $10}')" >> /home/$USER/logdate.txt
fi
