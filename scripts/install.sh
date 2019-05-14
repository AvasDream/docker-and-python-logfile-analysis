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
fi

chmod 744 /var/log/auth.log
if [ "$?" -ne 0 ]
then 
  echo "[!] Error while setting the auth.log file to world readable"
  exit 1
fi

docker build . -t pyauthlog
if [ "$?" -ne 0 ]
then 
  echo "[!] Error while building the dockerfile"
  exit 1
fi

# make monitor script executable
chmod 711 scripts/monitor.sh
if [ "$?" -ne 0 ]
then 
  echo "[!] Error while making monitor.sh script executable for everyone"
  exit 1
fi

# Add cron job
crontab -l > tmpcron && echo "0 3 * * *	$(pwd)/scripts/monitor.sh" >> tmpcron && crontab tmpcron && rm tmpcron
if [ "$?" -ne 0 ]
then 
  echo "[!] adding cron job"
  exit 1
fi

