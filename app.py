"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import json
from attrdict import AttrDict
from flask import Flask
from flask import request
import datetime
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

import logginghelper as logger
logger.init()

import confighelper as config
config.init()

import crud_actions as crud
print('done')

@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello World!"

@app.route('/server/entities/data/<reference>',methods=['GET'])
def getdata(reference):
    status, data = crud.getall(reference)
    response = json.dumps({'status':status,'data':data},default=jsonconverter)

    return response

@app.route('/server/entities/insert',methods=['POST'])
def insertdata():
    try:
        req = AttrDict(request.json)
        status, data = crud.insert(req.reference, req.client_data)
        response = json.dumps({'status':status,'data':data},default=jsonconverter)
    except Exception as e:
        print(str(e))

    return response

@app.route('/server/entities/update',methods=['POST'])
def updatedata():
    req = AttrDict(request.json)
    status, data = crud.update(req.reference, req.client_data)
    response = json.dumps({'status':status,'data':data},default=jsonconverter)

    return response

@app.route('/server/entities/delete',methods=['DELETE'])
def deletedata():
    req = AttrDict(request.json)
    status, data = crud.delete(req.reference, req.client_data)
    response = json.dumps({'status':status,'data':data},default=jsonconverter)

    return response


def jsonconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()[:-3]
    if isinstance(o, AttrDict):
        return dict(o)

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    PORT = 5555
    app.run(HOST, PORT)
