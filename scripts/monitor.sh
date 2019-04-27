#!/bin/bash
# Bash script for generating data input files 
cat /var/log/auth.log | grep "Failed password" | awk -F 'from' '{print $2}' | cut -d" " -f2 | uniq 2>&1 > /home/vgrimmeisen/log/$(date +%d-%m-%y)_ips.txt 
cat /var/log/auth.log | grep 'Failed password for' | awk -F 'invalid user' '{print $2}' | cut -d" " -f2 | awk 'NF' | uniq > /home/vgrimmeisen/log/$(date +%d-%m-%y)_users.txt
# cp /var/log/auth.log /home/vgrimmeisen/log/$(date +%d-%m-%y-%H:%m)_auth.log
