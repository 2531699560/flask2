#!/bin/bash
#sudo su
sed -i 's/^PASS_WARN_AGE.*/PASS_WARN_AGE 7/' /etc/login.defs
chage --warndays 7 root
chmod 0400 /etc/shadow  && chmod 0400 /etc/gshadow
echo "ClientAliveInterval 900" >> /etc/ssh/sshd_config
echo "ClientAliveCountMax 0" >> /etc/ssh/sshd_config
sed -i '/MaxAuthTries/d' /etc/ssh/sshd_config
echo "MaxAuthTries 5" >> /etc/ssh/sshd_config
