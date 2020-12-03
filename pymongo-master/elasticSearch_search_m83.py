# import json
# from collections import defaultdict
# from http import HTTPStatus
import pymongo as pymongo
import urllib.parse
import logging
# import requests
from elasticsearch import Elasticsearch
from pymongo import database, MongoClient


def connectToElastic(args):
    url = 'm83-es-master:9200'
    try:
        es = Elasticsearch(url)
        logging.info("Connection Established")
    except Exception as ex:
        logging.info("Cannot connect to Elastic Search" + ex)
    return es


def connectToMongo(args, collection):
    doc = args.get("__ow_headers")
    mongo = doc.get("mongo")
    mongo = mongo.split("=")
    mongo = mongo.__getitem__(1)
    mongo_connect_url = mongo.split(",")
    mongo_connect_url = mongo_connect_url.__getitem__(0)
    try:
        database = pymongo.MongoClient(mongo_connect_url)
    except:
        return error_response(500, "cannot connnect to mongodb")
    database = database.get_database()
    connect = database[collection]
    return connect


def error_response(error_code, msg):
    return {
        "body": {
            "code": error_code,
            "message": "Exception",
            "data": msg
        },
        "statusCode": error_code,
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
    value = args.get("search")
    # value = '10'
    data = []

    try:
        f = 0
        if value.isdigit():
            f = 1
            value = int(value)

        res = es.search(index='subscribers_v2', body={
            "query": {
                "bool": {
                    "should": [{
                        "match_phrase_prefix": {
                            "attachedAssets.assetName": value
                        }
                    },
                        {
                            "match_phrase_prefix": {
                                "attachedAssets.assetId": value
                            }
                        },
                        {
                            "match_phrase_prefix": {
                                "attachedAssets.assetType": value
                            }
                        },
                        {
                            "match_phrase_prefix": {
                                "clusterName": value
                            }
                        },
                        {
                            "match_phrase_prefix": {
                                "name": value
                            }
                        },
                        {
                            "match_phrase_prefix": {
                                "phone": str(value)
                            }
                        },
                        {
                            "match_phrase_prefix": {
                                "email": value
                            }
                        },
                        {
                            "match_phrase_prefix": {
                                "address": value
                            }
                        }
                    ]}
            }})

        for i in res['hits']['hits']:
            result = i["_source"]
            devices = result['attachedAssets']
            name = result['name']
            email = result['email']
            phone = result['phone']
            address = result['address']
            cluster_name = result['clusterName']
            if f == 1 and str(value) in phone:
                f = 3
            if f == 0 and value in [asset['assetName'] for asset in devices]:
                f = 2
            for j in devices:
                sub = {}
                if (f == 1 and str(value) in str(j['assetId'])) or (f == 2 and value in j['assetName']):
                    sub['id'] = j['id']
                    sub['assetId'] = j['assetId']
                    sub['assetType'] = j['assetType']
                    sub['assetName'] = j['assetName']
                    sub['name'] = name
                    sub['email'] = email
                    sub['phone'] = phone
                    sub['address'] = address
                    sub['clusterName'] = cluster_name
                    data.append(sub)
                elif f == 0:
                    sub['id'] = j['id']
                    sub['assetId'] = j['assetId']
                    sub['assetType'] = j['assetType']
                    sub['assetName'] = j['assetName']
                    sub['name'] = name
                    sub['email'] = email
                    sub['phone'] = phone
                    sub['address'] = address
                    sub['clusterName'] = cluster_name
                    data.append(sub)
                elif f == 3:
                    sub['id'] = j['id']
                    sub['assetId'] = j['assetId']
                    sub['assetType'] = j['assetType']
                    sub['assetName'] = j['assetName']
                    sub['name'] = name
                    sub['email'] = email
                    sub['phone'] = phone
                    sub['address'] = address
                    sub['clusterName'] = cluster_name
                    data.append(sub)

        # print(data)

    except:
        # print('error')
        data = []
    return success_response(data, 200)