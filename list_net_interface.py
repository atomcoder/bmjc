# coding = utf-8

import get_key


def list_net_interface():
    return get_key.get_key('NetInterface', 'SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\Interfaces')

if __name__ == "__main__":
    print('There are NetInterface:')
    for i in list_net_interface():
        for j in i:
            print(j[0], ':', j[1])
        print()
