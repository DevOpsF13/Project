#!/usr/bin/env python3

import os
import time
import shutil
from datetime import datetime


BACKUP_DIR = os.getenv("BACKUP_DIR", "backup")
BACKUP_INTERVAL = int(os.getenv("BACKUP_INTERVAL", 5))
SOURCE_FILE = "system-state.log"


os.makedirs(BACKUP_DIR, exist_ok=True)


last_mtime = None

print(f" Monitor backup activ: verifică '{SOURCE_FILE}' la fiecare {BACKUP_INTERVAL} secunde")
print(f" Backup-urile vor fi salvate în: '{BACKUP_DIR}'")

while True:
    if os.path.exists(SOURCE_FILE):
        current_mtime = os.path.getmtime(SOURCE_FILE)
        if last_mtime is None or current_mtime != last_mtime:
           
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_filename = f"system-state_{timestamp}.log"
            backup_path = os.path.join(BACKUP_DIR, backup_filename)
            
            shutil.copy2(SOURCE_FILE, backup_path)
            print(f"[{timestamp}] Backup salvat: {backup_path}")

            last_mtime = current_mtime
    else:
        print(f" Fișierul '{SOURCE_FILE}' nu există încă.")

    time.sleep(BACKUP_INTERVAL)
