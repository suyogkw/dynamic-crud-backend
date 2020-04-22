import pyodbc
import confighelper as config
import logginghelper as logger
from attrdict import AttrDict

connection = pyodbc.connect(config.connection_string,autocommit=True)

def execute(query, params=()):
    cursor = connection.cursor()
    cursor.execute(query, params)


def getdata(query, params=()):
    cursor = connection.cursor()
    cursor.execute(query,params)
    results = cursor.fetchall()
    result_set = [AttrDict({column[0]:res[i] for i,column in enumerate(cursor.description)}) for res in results]
    return result_set



