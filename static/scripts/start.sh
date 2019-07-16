#!/bin/bash
nohup /usr/local/nginx/sbin/nginx &
nohup /usr/bin/python /usr/bin/webhookit -c /alidata/services/webhookit/config/config.py -p 8000 &
nohup /usr/local/php/sbin/php-fpm &
