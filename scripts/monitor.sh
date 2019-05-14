#!/bin/bash
# Bash script for generating data input files 
d="/root/pyAuthLog/scripts"
cat /var/log/auth.log | grep "Failed password" | awk -F 'from' '{print $2}' | cut -d" " -f2 | uniq 2>&1 > $(pwd)/../input/$(date +%d-%m-%y)_ips.txt 
if [ "$?" -ne 0 ]
then
    echo "[!] Error while copying data" 
    exit 1
fi
echo "[*] Copied data in input directory"
docker run --rm -e DATE="$(date +%d-%m-%y)"  -v "$(pwd)/../:/home/pyauthlog" pyauthlog
if [ "$?" -ne 0 ]
then
    echo "[!] Error while executing docker container" 
    exit 1
fi

