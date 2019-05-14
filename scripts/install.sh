#!/bin/bash

if [ "$EUID" -ne 0 ]
then 
  echo "[!] Please execute this script as root"
  exit 1
fi

docker --version
if [ "$?" -ne 0 ]
then
    echo "[!] Please install docker first!"
    exit 1
fi

cd .. && mkdir data && mkdir output
if [ "$?" -ne 0 ]
then 
  echo "[!] Error while creating /data and /output"
  exit 1
else
  echo "[*] created /data and /output directory"
fi

chmod 744 /var/log/auth.log
if [ "$?" -ne 0 ]
then 
  echo "[!] Error while setting the auth.log file to world readable"
  exit 1
else
  echo "[*] setting permissions on auth.log"
fi

docker build . -t pyauthlog > /dev/null
if [ "$?" -ne 0 ]
then 
  echo "[!] Error while building the dockerfile"
  exit 1
else
  echo "[*] Dockerimage build"
fi

# make monitor script executable
chmod 711 scripts/monitor.sh
if [ "$?" -ne 0 ]
then 
  echo "[!] Error while making monitor.sh script executable for everyone"
  exit 1
else 
  echo "[*] Making monitor.sh script executable"
fi


crontab -l
if [ "$?" -ne 0 ]
then
  echo "[*] crontab is empty creating from scratch"
  echo "0 3 * * * $(pwd)/scripts/monitor.sh" >> tmpcron && crontab tmpcron && rm tmpcron
else
  echo "[*] creating crontab entry"
  crontab -l > tmpcron && echo "0 3 * * * $(pwd)/scripts/monitor.sh" >> tmpcron && crontab tmpcron && rm tmpcron
fi
if [ "$?" -ne 0 ]
then 
  echo "[!] Error while adding cron job"
  exit 1
fi

