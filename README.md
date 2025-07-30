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