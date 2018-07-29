from google.cloud import datastore
import os
import json
from flask import jsonify
import logging
import datetime

client = datastore.Client()

def submitMSG(request):
    key = client.key('Message')
    task = datastore.Entity(key)
    task.update({
        'url': request.args['url'],
        'msg': request.args['msg'],
        'author': request.args['author'],
        'approved': False,
        'time': datetime.datetime.utcnow(),
    })  
    client.put(task)
    return "Thanks for your comment. It'll be reviewed shortly."