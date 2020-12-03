import json
from collections import defaultdict
from http import HTTPStatus
import pymongo as pymongo
import urllib.parse
import logging
import re
from pymongo import database, MongoClient
from elasticsearch import Elasticsearch
from datetime import datetime


def connectToElastic(args):
    url = 'm83-es-master:9200'
    try:
        es = Elasticsearch(url)
        logging.info("Connection Established")
    except Exception as ex:
        logging.info("Cannot connect to Elastic Search" + ex)
    return es


def connectToMongo(client, collection):
    coll = client.get_database()
    connect = coll[collection]
    return connect


def getMongoClient(args):
    client = None
    doc = args.get("__ow_headers")
    mongo = doc.get("mongo")
    mongo = mongo.split("=")
    mongo = mongo.__getitem__(1)
    mongo_connect_url = mongo.split(",")
    mongo_connect_url = mongo_connect_url.__getitem__(0)
    try:
        client = pymongo.MongoClient(mongo_connect_url)
    except:
        return error_response(500, "Cannot connnect to Mongo Database")
    return client


def closeConnection(client):
    try:
        client.close()
    except:
        return error_response(500, "Cannot close Connection to Mongo Database")
    return None


def error_response(http_status, message):
    return {
        "body": {
            "code": http_status,
            "message": "Exception",
            "data": message
        },
        "statusCode": http_status,
        "headers": {'Content-Type': 'application/json'}
    }


def success_response(data, status_code):
    return {
        "body": {
            "code": 0,
            "message": "Request Completed Successfully",
            "data": data
        },
        "statusCode": status_code,
        "headers": {'Content-Type': 'application/json'}
    }


def main(args):
    es = connectToElastic(args)
    client = getMongoClient(args)
    con_subscribers = connectToMongo(client, 'subscribersV2_cccab979')
    con_registration = connectToMongo(client, 'inventoryV2_cccab979')
    con_cluster = connectToMongo(client, 'clustersV2_cccab979')
    # subscriber_id = '5c2c7752c4ce11ea8d727ed498f901c6'
    # name = 'testing'
    # email = 'test@gmail.com'
    # phone = '9908437647'
    # cluster_id = '322507ecabbf11eaa57e5a2203e495a9'
    # address = 'Andheri, Maharashtra 400053, India'
    # lat = 19.113645
    # lng = 19.113645
    # data = attached_assets = [{'assetId': 7018,'assetName': 'SFP7018','assetType': 'SFP','assetVersion': '2.3.5','id': '324850896575800500530024','checked': True},{'assetId': 7019,'assetName': 'SFP7019','assetType': 'SFP','assetVersion': '2.3.5','id': '324850896575800500530027','checked': True}]
    name = args.get('name')
    subscriber_id = args.get('id')
    cluster_id = args.get('clusterId')
    phone = args.get('phone')
    address = args.get('address')
    email = args.get('email')
    attached_assets = args.get('attachedAssets')
    lat = args.get('lat')
    lng = args.get('lng')
    timestamp = datetime.now().timestamp()
    updated_at = int(timestamp * 1000)
    updated_by = 'System'
    assigned_date = datetime.fromtimestamp(int(timestamp))

    if type(name) != str:
        return error_response(400, 'Invalid Name')
    elif type(email) != str:
        return error_response(400, 'Invalid Email')
    elif type(phone) != str:
        return error_response(400, 'Invalid Phone Number')
    elif type(address) != str:
        return error_response(400, 'Invalid Address')
    # else:
    try:
        cluster_check = con_cluster.find({'id': cluster_id})
        old_data = es.get(index='subscribers_v2', id=subscriber_id)['_source']
        old_email = old_data['email']
        old_phone = old_data['phone']
        old_assets = [asset['id'] for asset in old_data['attachedAssets']]

        if old_email != email:
            email_check = con_subscribers.find({'email': email})
            if (email_check.count()) != 0:
                return error_response(400, 'Email already exists')
        elif old_phone != phone:
            phone_check = con_subscribers.find({'phone': phone})
            if (phone_check.count()) != 0:
                return error_response(400, 'Phone number already exists')
        elif (cluster_check.count()) == 0:
            return error_response(400, 'Cluster does not exists')

        cluster_name = ''
        for i in cluster_check:
            cluster_name = i['name']

        e_query = e_query = {'id': subscriber_id, 'clusterId': cluster_id, 'clusterName': cluster_name, 'name': name,
                             'email': email, 'phone': phone, 'address': address, 'attachedAssets': attached_assets}

        query = {'id': subscriber_id, 'clusterId': cluster_id, 'name': name, 'email': email, 'phone': phone,
                 'attachedAssets': attached_assets, 'assetCount': len(attached_assets), 'address': address, 'lat': lat,
                 'lng': lng, 'updatedAt': updated_at, 'updatedBy': updated_by}

        result = es.index(index='subscribers_v2', id=subscriber_id, body=e_query)
        con_subscribers.update_one({'id': subscriber_id}, {'$set': query})
        # assets=[asset['assetId'] for asset in attached_assets]
        for k in old_assets:
            con_registration.update_one({'id': k}, {
                '$set': {'isAssigned': False, 'assignedDate': None, 'UnassignedDate': assigned_date,
                         'subscriberId': None, 'assetName': 'SFP' + str(k)}})
        for k in attached_assets:
            con_registration.update_one({'id': k['id']}, {
                '$set': {'isAssigned': True, 'assignedDate': assigned_date, 'UnassignedDate': None,
                         'subscriberId': subscriber_id, 'assetName': k['assetName']}})
        data = ['Success']
        return success_response(data, 200)
    except:
        return error_response(400, 'Error occured while updating in DB')
    closeConnection(client)  