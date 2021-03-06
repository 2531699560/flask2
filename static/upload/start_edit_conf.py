#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from crontab import CronTab


def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        # print(files) # 当前路径下所有非目录子文件
        conf = []
        for j in files:
            if "conf"  == j[-4:]:
                if  j == "zong.conf":
                    continue
                else:
                    conf.append(j)

        return conf


def edit_file(file_name,change_content):
    for j in file_name:
        file_name = '/usr/local/nginx/conf/vhost/'+ j
        print(file_name)
        # edit_file(j,content,zong)
        file_read = open(file_name,'r')
        f_read = file_read.readlines()
        file_read.close()
        file_write = open(file_name, 'w')
        start = 0
        loc_list = []
        for i in f_read:
            # print(i)
            if "include enable-php.conf;" in i:
                start = f_read.index(i) - 1
            if "location / {" in i:
                loc = f_read.index(i)
                for j in range(0,5):
                    loc_list.append(loc+j)
        for j in range(0,len(f_read)):
            if j == start:
                file_write.write(change_content)
            elif j in loc_list:
                file_write.write('#'+f_read[j])
            else:
                file_write.write(f_read[j])
        file_write.close()


def backup_conf(file_name,back_file):
    zong = []
    print(file_name)
    f_zong = open(back_file, 'w')
    for j in file_name:
        file_name = '/usr/local/nginx/conf/vhost/' + j
        file_read = open(file_name,'r')
        f_read = file_read.readlines()
        file_read.close()
        for i in f_read:
            zong.append(i)
    for k in zong:
        f_zong.write(k)
    f_zong.close()


#关闭所有crontab任务
def cron_():
    my_user_cron = CronTab(user="www")
    for job in my_user_cron:
        job.enable(False)
        print(job)
    my_user_cron.write()



# print(file_name('./'))
if __name__ == '__main__':
    content = """
        location / {
                try_files '' /index.html;
        }
        location =/index.html {
                index  index.html index.htm;
        }
    """
    back_file = '/usr/local/nginx/conf/vhost/zong.conf'
    file_name = file_name('/usr/local/nginx/conf/vhost/')
    backup_conf(file_name,back_file)
    edit_file(file_name,content)
    cron_()

