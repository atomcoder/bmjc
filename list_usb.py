# coding = utf-8

import winreg
import ms_time



def list_usb(patch):
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, patch)
    key_value_list = []

    try:
        for i in range(winreg.QueryInfoKey(key)[0]):
            sub_key_name = winreg.EnumKey(key, i)
            sub_key = winreg.OpenKey(key, sub_key_name)
            sub_key_time = ms_time.ms_datetime(winreg.QueryInfoKey(sub_key)[2])
            sub_key_value_list = list()
            for j in range(winreg.QueryInfoKey(sub_key)[1]):
                sub_key_value = winreg.EnumValue(sub_key, j)
                sub_key_value_list.append(sub_key_value)
            sub_key_value_list = sorted(sub_key_value_list)
            sub_key_value_list.insert(0, ('Time', sub_key_time.strftime('%Y-%m-%d,%H:%M:%S')))
            sub_key_value_list.insert(0, ('Interface', sub_key_name))
            key_value_list.append(sub_key_value_list)
            sub_key.Close()
    except WindowsError:
        print()
    key.Close()
    if __name__ == "__main__":
        for i in key_value_list:
            print(i)


if __name__ == '__main__':
    list_usb()
