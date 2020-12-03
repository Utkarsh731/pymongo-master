import datetime as dt
time="2020-11-06T12:40:23.688Z"
date_time_obj = dt.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')
print('Date:', date_time_obj.timestamp()*1000)

total_trip_time=1604916402353
started_trip_time=1604662874439
total_hours=( total_trip_time - started_trip_time )/(3600000)
print(total_hours)
if total_hours>20:
    if total_hours>=24:
        remaining_hours=total_hours%24
        print(remaining_hours)
        if remaining_hours>20:
            print("res")