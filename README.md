# Project
# System State Monitor

Un script Bash care monitorizează periodic resursele sistemului și scrie informațiile într-un fișier `system-state.log`. La fiecare rulare, fișierul este suprascris, păstrând doar ultimele date colectate.

## Descriere

Scriptul colectează și loghează următoarele informații:

-  Utilizarea memoriei (RAM)
-  Utilizarea spațiului pe disc
-  Gradul de încărcare al CPU-ului
-  Numărul de procese active în sistem

## Frecvență

Monitorizarea se face **la fiecare 13 secunde**, într-o buclă infinită, până când scriptul este oprit manual.

## Fișiere generate

- `system-state.log` — fișierul în care se scriu datele de sistem. Acesta este **suprascris complet** la fiecare ciclu de execuție.

## Rulare

### 1. Fă scriptul executabil:
```bash
chmod +x system_state.sh

2. Rulează scriptul:

./system_state.sh

3. Oprește execuția:

Apasă Ctrl + C pentru a opri rularea buclei.

Scriptul trebuie rulat de un utilizator cu drepturi suficiente pentru a accesa comenzile free, df, top, și ps.



Script: Monitorizare și Backup pentru un Fișier Log

Descriere Generală

Acest script în Python monitorizează un fișier (system-state.log, implicit) și creează automat un backup de fiecare dată când detectează o modificare a conținutului său. Backup-urile sunt salvate cu un timestamp în nume, într-un director dedicat.


 Funcționalitate

    Verifică periodic existența și modificarea fișierului sursă.

    Dacă fișierul a fost modificat, creează o copie de backup cu un nume unic bazat pe dată și oră.

    Salvează toate backup-urile într-un director specificat.

    Intervalul de verificare și calea fișierelor pot fi configurate prin variabile de mediu.

 Structura Scriptului
🔸 
Importuri :

import os
import time
import shutil
from datetime import datetime

Importă modulele necesare:

    os: Interacțiune cu sistemul de fișiere.

    time: Pentru controlul pauzelor între verificări.

    shutil: Pentru copierea fișierelor.

    datetime: Pentru generarea timestamp-urilor.

🔸 Configurări (cu fallback-uri implicite)

BACKUP_DIR = os.getenv("BACKUP_DIR", "backup")
BACKUP_INTERVAL = int(os.getenv("BACKUP_INTERVAL", 5))
SOURCE_FILE = os.getenv("SOURCE_FILE", "system-state.log")

    BACKUP_DIR: Directorul unde vor fi salvate backup-urile. Implicit: backup/.

    BACKUP_INTERVAL: Intervalul de timp (în secunde) între verificări. Implicit: 5 secunde.

    SOURCE_FILE: Calea către fișierul care trebuie monitorizat. Implicit: system-state.log.

🔸 Creare director backup (dacă nu există)

os.makedirs(BACKUP_DIR, exist_ok=True)

🔸 Mesaje informative la pornire

print(...)

Afișează detalii despre configurările curente.
🔁 Bucla principală (while True)

Verifică constant dacă fișierul a fost modificat:

    Existență fișier: Se verifică dacă SOURCE_FILE există.

    Modificare detectată: Se compară mtime curent cu ultimul salvat.

    Backup: Dacă fișierul s-a modificat:

        Se generează un nume de fișier cu timestamp.

        Se copiază fișierul în directorul de backup.

    Așteptare: Scriptul așteaptă BACKUP_INTERVAL secunde înainte de a reporni verificarea.

    Output

La fiecare modificare detectată, se creează un fișier nou în format:backup/system-state_YYYYMMDD_HHMMSS.log


Considerații

    Scriptul rulează la infinit. Pentru a-l opri, se folosește Ctrl+C.

    Nu monitorizează modificări în conținut, doar data ultimei modificări (mtime).

    Backup-urile pot consuma mult spațiu dacă fișierul sursă se modifică frecvent.

Cerințe

    Python 3.x

    Permisiuni de citire pentru fișierul sursă

    Permisiuni de scriere în directorul de backup



    #  Docker Container: Monitorizare `system-state.sh`

## Descriere

Acest container Docker este bazat pe imaginea oficială `ubuntu:latest` și este configurat pentru a rula un script shell numit `system-state.sh`. Este util pentru sarcini de monitorizare sau întreținere automate, direct dintr-un mediu izolat și portabil.

---

##  Structura Dockerfile

```Dockerfile
FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    bash \
    procps \
    coreutils \
    util-linux \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /sh-container

COPY system-state.sh .

RUN chmod +x system-state.sh

CMD ["./system-state.sh"]

🔧 Pași pentru Build & Run
🔨 1. Build imaginea Docker

Asigură-te că Dockerfile și scriptul system-state.sh se află în același director, apoi rulează:

docker build -t system-monitor .

🚀 2. Rulează containerul

docker run --rm system-monitor

    * --rm va șterge containerul după ce se oprește (opțional).

   Componentele imaginii
Componentă	    Descriere
ubuntu:latest	Imagine de bază - Ubuntu Linux (ultima versiune stabilă)
bash	        Shell-ul necesar pentru rularea scriptului .sh
procps	        Utilitare precum ps, top, uptime, etc.
coreutils	    Utilitare GNU de bază (ls, cat, echo, etc.)
util-linux	    Comenzi precum dmesg, fdisk, kill, mount, etc.

  Structura containerului
Locație	        Descriere
/sh-container	Directorul de lucru în container
system-state.sh	Scriptul copiat și executat automat

Informatii necesare:

    Imaginea se bazează pe ubuntu:latest, care poate varia în timp. Pentru consistență, recomand folosirea unei versiuni fixe (ubuntu:22.04).

    


    #  Dockerfile - Documentație pentru backup_system_log.py


Acest Dockerfile construiește o imagine Docker care rulează un script Python (backup_system_log.py) într-un container ușor, pe baza unei imagini python:3.11-slim. Scopul scriptului este realizarea unui backup periodic al unui fișier de sistem, cu un interval de timp configurabil printr-o variabilă de mediu.

##  Structura Dockerfile-ului

```dockerfile
FROM python:3.11-slim

WORKDIR /py-container

    Setează directorul de lucru în container la /py-container.

    Toate comenzile ulterioare vor fi executate din acest director.


COPY backup_system_log.py .

    Copiază scriptul local backup_system_log.py în directorul de lucru al containerului.

CMD ["python3", "backup_system_log.py"]

    Specifică comanda implicită care va fi rulată când containerul pornește.

    Rulează scriptul Python care conține logica de backup.


Comenzi utile:

docker build -t backup-logger . - Build imaginea Docker
docker run backup-logger - Rulează containerul
docker run -d --name backup-container -e BACKUP_INTERVAL=10 backup-logger -Rulează containerul în fundal (detached)



    #  Documentație `docker-compose.yml`

Acest fișier `docker-compose.yml` definește un mediu format din două servicii Docker:  
1. `system-state` – un container care generează fișierul de loguri `system-state.log`.  
2. `backup` – un container care face backup la acest fișier la un interval configurabil.

---

##  Versiune Compose

```yaml
version: "3.9"

    Specifică versiunea de sintaxă docker-compose.

    Versiunea 3.9 este compatibilă cu Docker 20.10+ și oferă suport pentru volume, variabile de mediu și altele.

 Servicii:

🔹 system-state
🔹 backup

Volume partajat:
Volumul shared-logs este definit global și este montat în ambele containere.

Este folosit pentru a face schimb de fișiere între servicii, fără rețea sau transfer extern.
Schimbul de date între containere se face exclusiv prin volumul comun shared-logs.



Utilizare:

Build imaginile prin urmatoarele comenzi:

docker build -t system-state ./system-state
docker build -t back_up ./backup

Pornește serviciile:

docker-compose up -d - Rulează containerele în fundal.

                     - Logurile și backup-urile vor începe automat, conform configurației.

Oprește serviciile:

docker-compose down      



# 🚀 Jenkins Pipeline - Documentație

Acest `Jenkinsfile` definește un pipeline declarativ care rulează pe un agent cu label-ul `ubuntu`, realizează checkout dintr-un repository GitHub, apoi construiește și publică o imagine Docker într-un registry Docker Hub.

---

## 🧩 Structura Pipeline-ului

```groovy
pipeline {
    agent {
        label "ubuntu"
    }

    stages {
        ...
    }
}

Etape ale Pipeline-ului:

Stage: Git checkout - Clonează codul sursă din repository-ul Git specificat.
Stage: Build Image - Construiește o imagine Docker din Dockerfile-ul aflat în repository.


Cerințe preliminare :

Pentru ca pipeline-ul să ruleze cu succes:

Docker instalat pe agentul Jenkins.

Credențiale GitHub configurate în Jenkins (folosind credentialsId).

Autentificare Docker Hub (folosind docker login înainte de push).

Dockerfile valid în directorul rădăcină al repository-ului.

Agentul Jenkins trebuie să aibă label-ul ubuntu.




