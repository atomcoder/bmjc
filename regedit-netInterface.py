# coding = utf-8

import winreg
import datetime

TimedeltaPYtoMS = datetime.datetime(1970, 1, 1, 0, 0) - datetime.datetime(1601, 1, 1, 0, 0)

Key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces')
KeyValueList = []

try:
    for i in range(winreg.QueryInfoKey(Key)[0]):
        SubKeyName = winreg.EnumKey(Key, i)
        SubKey = winreg.OpenKey(Key, SubKeyName)
        SubKeyTime = datetime.datetime.fromtimestamp((winreg.QueryInfoKey(SubKey)[2]/10000000) -
                                                     TimedeltaPYtoMS.total_seconds())  # Time
        SubKeyValueList = list()
        for j in range(winreg.QueryInfoKey(SubKey)[1]):
            SubKeyValue = winreg.EnumValue(SubKey, j)
            SubKeyValueList.append(SubKeyValue)
        SubKeyValueList = sorted(SubKeyValueList)
        SubKeyValueList.insert(0, ('Time', SubKeyTime.strftime('%Y-%m-%d,%H:%M:%S')))
        SubKeyValueList.insert(0, ('Interface', SubKeyName))
        KeyValueList.append(SubKeyValueList)
        SubKey.Close()
except WindowsError:
    print()
Key.Close()
for i in KeyValueList:
    print(i)

