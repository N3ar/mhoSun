import datetime


def convert(utc_time):
    print(utc_time.split(' '))
    local_time = datetime.datetime.strptime(utc_time[0], '%H:%M:%S')
    print(local_time)
