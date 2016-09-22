# coding = utf-8
import datetime


def ms_datetime(ms_datetime_var):
    return datetime.datetime.fromtimestamp((ms_datetime_var / 10000000) -
                                           (datetime.datetime(1970, 1, 1, 0, 0) - datetime.datetime(1601, 1, 1, 0, 0))
                                           .total_seconds())  # MSTime to PythonTime
if __name__ == '__main__':
    print('MSTime is since Jan,1,1601.\nPythonTime is since Jan,1,1970.')
    print('In RegEdit the key was last modified (if available) as 100\'s of nanoseconds since Jan 1, 1601')
    print('Now is', datetime.datetime.now())
