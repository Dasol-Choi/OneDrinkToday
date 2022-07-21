
from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

client = MongoClient('mongodb://ReadOnly_5rink:to5ay5rinks@3.36.229.90', 27017)
db = client.To5ay5rink

def search_name (keyword):
    result = list(db.Cocktails.find(
        {'$or': [
            {'name_kor': {'$regex': keyword}},
            {'name': {'$regex': keyword, '$options': 'i'}}
        ]
        },
        {'_id': False}
    ))

    return result