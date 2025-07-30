#!/bin/bash

LOG_FILE="system-state.log"
INTERVAL=5  # Intervalul în secunde

echo "=== Pornire monitorizare sistem (log în $LOG_FILE, la fiecare $INTERVAL secunde) ==="

while true; do
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")

    {
        echo "[$TIMESTAMP] --- SYSTEM STATUS ---"

        echo " Memory usage:"
        free -h

        echo " Disk usage:"
        df -h

        echo "⚙ CPU load:"
        top -bn1 | grep "Cpu(s)"

        echo " Active processes: $(ps -e --no-headers | wc -l)"

        echo ""
    } > "$LOG_FILE"  # suprascrie tot conținutul la fiecare ciclu

    sleep "$INTERVAL"
done

