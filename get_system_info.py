# coding = utf-8

import os
import platform
import psutil
import datetime


boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()) #开机时间
cpu_count = psutil.cpu_count() #CPU数量
cpu_percent = psutil.cpu_percent(interval = 0.1, percpu = True)#当前CPU占用率







HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkCards\8
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\Tcpip\Parameters\Adapters
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\NetworkList\Nla\Cache\Intranet
HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\NetworkCards\8
HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\0007
HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\DeviceClasses\{ad498944-762f-11d0-8dcb-00c04fc3358c}\##?#PCI#VEN_8086&DEV_100F&SUBSYS_075015AD&REV_01#4&3ad87e0a&0&0888#{ad498944-762f-11d0-8dcb-00c04fc3358c}\#{51244D51-F51E-4250-A2FA-313B0A5928A6}
HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Network\{4D36E972-E325-11CE-BFC1-08002BE10318}\{51244D51-F51E-4250-A2FA-313B0A5928A6}
HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Control\Network\{4D36E972-E325-11CE-BFC1-08002BE10318}\{FB3AAA2C-6592-414D-8BD7-22099CCCAFFB}\Connection
HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\services\{51244D51-F51E-4250-A2FA-313B0A5928A6}
HKEY_LOCAL_MACHINE\SYSTEM\ControlSet002\services\Tcpip\Parameters\Interfaces\{51244D51-F51E-4250-A2FA-313B0A5928A6}
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Class\{4D36E972-E325-11CE-BFC1-08002BE10318}\0007
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\Tcpip\Parameters\Interfaces\{51244D51-F51E-4250-A2FA-313B0A5928A6}