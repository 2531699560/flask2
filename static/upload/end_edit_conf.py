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

def huifu(f_zong):
    index_ = f_zong.readlines()
    edit_list = []
    f_zong.close()
    for j in range(0,len(index_)):
        # print(j)
        if "server" == index_[j].strip("").strip("\n"):
            # print(j)
            edit_list.append(j)
    edit_list.append(len(index_)-1)
    cont = 0
    # print(edit_list)
    for j in file_name("/usr/local/nginx/conf/vhost/"):
        # print(j,cont)
        if cont == len(edit_list) -1:
            start = edit_list[-2]
            end = edit_list[-1]
        else:
            start = edit_list[cont]
            end = edit_list[cont + 1]
        # print(start,end)
        content = index_[start:end]
        print(content)
        cont += 1
        f_write = open(j,'w')
        for k in content:
            f_write.write(k)
        f_write.close()


#开启任务
def cron_():
    my_user_cron  = CronTab(user = "www")
    for job in my_user_cron:
        if "crontab/repayment/index" in str(job):
            job.enable(False)
        else:
            job.enable()
    my_user_cron.write()
    for i in my_user_cron:
        print(i)


if __name__ == '__main__':
    f_zong = open('/usr/local/nginx/conf/vhost/', 'r')
    huifu(f_zong)
    f_zong.close()
    cron_()