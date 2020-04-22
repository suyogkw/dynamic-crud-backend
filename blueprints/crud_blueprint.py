
from flask import Blueprint
from utilities import jsonconverter
import crud_actions as crud
import json
from flask import request
from attrdict import AttrDict

crud_blueprint = Blueprint('crud_blueprint', __name__, url_prefix='/server/entities')

@crud_blueprint.route('/data/<reference>',methods=['GET'])
def getdata(reference):
    status, data = crud.getall(reference)
    response = json.dumps({'status':status,'data':data},default=jsonconverter)

    return response

@crud_blueprint.route('/insert',methods=['POST'])
def insertdata():
    try:
        req = AttrDict(request.json)
        status, data = crud.insert(req.reference, req.client_data)
        response = json.dumps({'status':status,'data':data},default=jsonconverter)
    except Exception as e:
        print(str(e))

    return response

@crud_blueprint.route('/update',methods=['POST'])
def updatedata():
    req = AttrDict(request.json)
    status, data = crud.update(req.reference, req.client_data)
    response = json.dumps({'status':status,'data':data},default=jsonconverter)

    return response

@crud_blueprint.route('/delete',methods=['DELETE'])
def deletedata():
    req = AttrDict(request.json)
    status, data = crud.delete(req.reference, req.client_data)
    response = json.dumps({'status':status,'data':data},default=jsonconverter)

    return response


