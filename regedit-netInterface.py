import winreg

Key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces')
KeyValueList = []

try:
    for i in range(winreg.QueryInfoKey(Key)[0]):
        SubKeyName = winreg.EnumKey(Key, i)
        SubKey = winreg.OpenKey(Key, SubKeyName)
        SubKeyValueList = list()
        for j in range(winreg.QueryInfoKey(SubKey)[1]):
            SubKeyValue = winreg.EnumValue(SubKey, j)
            SubKeyValueList.append(SubKeyValue)
        SubKeyValueList = sorted(SubKeyValueList)
        SubKeyValueList.insert(0, ('Interface', SubKeyName))
        KeyValueList.append(SubKeyValueList)
        SubKey.Close()
except WindowsError:
    print()
Key.Close()
for i in KeyValueList:
    print(i)

