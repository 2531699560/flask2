#!/bin/bash
for i in `yum check-update | grep systemd | egrep "^system" | awk '{print $1}'`
do
yum -y update $i 
done
