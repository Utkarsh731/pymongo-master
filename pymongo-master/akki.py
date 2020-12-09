import pymongo
import urllib.parse
from datetime import datetime


def mongoConnectProd(tenant_name):
    username = urllib.parse.quote_plus('m83app_read')
    password = urllib.parse.quote_plus('qwerty@123')
    myclient = pymongo.MongoClient('mongodb://%s:%s@localhost:27018' % (username, password))
    return myclient[tenant_name]


prodDB = mongoConnectProd('demosales_1584380202775')

data = []

con_tracking = prodDB['ETL_analytics_TS101TrackingPacket_cc8a4220']
con_device = prodDB['ev_deviceDetails_cc8a4220']

first_timestamp = 1604773800000
interval = 86400000
last_timestamp = 1607365800000

devices = con_device.distinct('id')

for i in range(first_timestamp, last_timestamp, interval):
    timestamp = i + interval

    for d in con_device.find({'id': {'$in': devices}}):
        start_distance = 0
        distance = 0
        vehicle_id = d['vehicleNum']
        sim = d['simNum']
        imei = d['imeiNum']
        update = False
        date = None
        location = None

        for t in con_tracking.find({'deviceId': d['id'], 'timestamp': {'$gte': i, '$lt': timestamp}}).sort('timestamp',
                                                                                                           1):
            update = True
            ad = float(t['accumulatedDistance'])
            location = t['latitude'] + ',' + t['longitude']
            date_string = str(datetime.fromtimestamp(t['timestamp'] / 1000)).split(' ')[0].split('-')
            date = date_string[2] + '-' + date_string[1] + '-' + date_string[0]
            if start_distance == 0:
                start_distance = ad
            else:
                distance = abs(ad - start_distance)
                start_distance = ad

        if update:
            data.append({'deviceId': d['id'], 'vehicleNum': vehicle_id, 'sim': sim, 'imei': imei, 'location': location,
                         'kms': distance, 'date': date})

print(data)