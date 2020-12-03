import json
from collections import defaultdict
from http import HTTPStatus
import pymongo as pymongo
import urllib.parse
import logging
import uuid
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
    data = []
    es = connectToElastic(args)
    client = getMongoClient(args)
    con_subscribers = connectToMongo(client, 'subscribersV2_cccab979')
    con_registration = connectToMongo(client, 'inventoryV2_cccab979')
    con_cluster = connectToMongo(client, 'clustersV2_cccab979')
    timestamp = datetime.now().timestamp()
    name = args.get('name')
    email = args.get('email')
    phone = args.get('phone')
    cluster_id = args.get('clusterId')
    address = args.get('address')
    lat = args.get('lat')
    lng = args.get('lng')
    attached_assets = args.get('attachedAssets')
    # name = 'test'
    # email = 'testing@gmial.com'
    # phone = '9990999009'
    # cluster_id = 800001
    # address = 'Rajouri Garden'
    # lat = 28.646980
    # lng = 77.125660
    # attached_assets = [{'assetId': 101,'assetType': 'SFP','id': '324948705371801900390029','assetName': 'SFP101'}]
    created_at = updated_at = int(timestamp * 1000)
    assigned_date = datetime.fromtimestamp(int(timestamp))
    created_by = updated_by = 'System'

    if type(name) != str:
        return error_response(400, 'Invalid Name')
    elif type(email) != str:
        return error_response(400, 'Invalid Email')
    elif type(phone) != str:
        return error_response(400, 'Invalid Phone Number')
    elif type(address) != str:
        return error_response(400, 'Invalid Address')

    email_check = con_subscribers.find({'email': email})
    phone_check = con_subscribers.find({'phone': phone})
    cluster_check = con_cluster.find({'id': cluster_id})
    if (email_check.count()) != 0:
        return error_response(400, 'Email already exists')
    elif (phone_check.count()) != 0:
        return error_response(400, 'Phone number already exists')
    elif (cluster_check.count()) == 0:
        return error_response(400, 'Cluster does not exists')

    subscriber_id = (uuid.uuid1()).hex
    # else:
    try:
        cluster_name = ''
        for i in con_cluster.find({'id': cluster_id}):
            cluster_name = i['name']
        e_query = {'id': subscriber_id, 'clusterId': cluster_id, 'clusterName': cluster_name, 'name': name,
                   'email': email, 'phone': phone, 'address': address, 'attachedAssets': attached_assets}
        query = {'id': subscriber_id, 'clusterId': cluster_id, 'name': name, 'email': email, 'phone': phone,
                 'address': address, 'attachedAssets': attached_assets, 'assetCount': len(attached_assets), 'lat': lat,
                 'lng': lng, 'updatedAt': updated_at, 'createdAt': created_at, 'createdBy': created_by,
                 'updatedBy': updated_by}
        result = es.index(index='subscribers_v2', id=subscriber_id, body=e_query)
        con_subscribers.insert_one(query)

        for i in attached_assets:
            # data=['yes']
            con_registration.update_one({'id': i['id']}, {
                '$set': {'isAssigned': True, 'assignedDate': assigned_date, 'subscriberId': subscriber_id,
                         'assetName': i['assetName']}})

        data = ['Success']
        return success_response(data, 200)
    except:
        return error_response(HTTPStatus.BAD_REQUEST.value, 'Error occured while inserting in DB')
    closeConnection(client)