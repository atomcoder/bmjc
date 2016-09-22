# coding = utf-8

import winreg
import ms_time


Key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces')
KeyValueList = []

try:
    for i in range(winreg.QueryInfoKey(Key)[0]):
        SubKeyName = winreg.EnumKey(Key, i)
        SubKey = winreg.OpenKey(Key, SubKeyName)
        SubKeyTime = ms_time.ms_datetime(winreg.QueryInfoKey(SubKey)[2])
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
if __name__ == "__main__":
    for i in KeyValueList:
        print(i)
