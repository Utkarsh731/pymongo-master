import json
from collections import defaultdict
from http import HTTPStatus
import pymongo as pymongo
import urllib.parse
import logging
# import requests
# import re
from elasticsearch import Elasticsearch
from pymongo import database, MongoClient
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
    con_subscriber = connectToMongo(client, 'subscribersV2_cccab979')
    # con_cluster=connectToMongo(args,'clusters_cccab979')
    con_inventory = connectToMongo(client, 'inventoryV2_cccab979')
    subscriber_id = args.get("id")
    assigned_date = datetime.now()

    if type(subscriber_id) == None:
        return error_response(HTTPStatus.BAD_REQUEST.value, "Invalid Input")

    query = {"id": subscriber_id}
    doc = con_subscriber.find(query)
    if doc.count() == 0:
        return error_response(HTTPStatus.BAD_REQUEST.value, "No Matching Data Found")
    try:
        old_assets = [asset['id'] for asset in
                      es.get(index='subscribers_v2', id=subscriber_id)['_source']['attachedAssets']]
        con_subscriber.delete_one(query)
        result = es.delete(index='subscribers_v2', id=subscriber_id)

        for k in old_assets:
            # for i in con_cluster.find({'attachedAssets':asset_id}):
            #   cluster_id = i['id']
            #   cluster_assets  = i['attachedAssets']
            #   cluster_assets.remove(asset_id)
            #   if len(cluster_assets) == 0:
            #     con_cluster.delete_one({'id':cluster_id})
            # else:
            # con_cluster.update_one({'id':cluster_id},{'$set':{'attachedAssets':cluster_assets,'assetCount':len(cluster_assets)}})
            con_inventory.update_one({"id": k}, {
                "$set": {"isAssigned": False, "assignedDate": None, "UnassignedDate": assigned_date,
                         "subscriberId": None, "assetName": "SFP" + str(k)}})
        data = result['result']
        return success_response(data, 200)
    except:
        return error_response(HTTPStatus.BAD_REQUEST.value, "Error occured while deleting from DB")
    closeConnection(client)