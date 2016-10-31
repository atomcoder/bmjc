# coding = utf-8

import os
import platform
import psutil
import datetime


boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()) #开机时间
cpu_count = psutil.cpu_count() #CPU数量
cpu_percent = psutil.cpu_percent(interval=0.1, percpu=True)#当前CPU占用率


print(boot_time, cpu_count, cpu_percent)
