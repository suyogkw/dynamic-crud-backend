import pyodbc
import confighelper as config
import logginghelper as logger
from attrdict import AttrDict

connection = pyodbc.connect(config.connection_string)

def execute(query):
    cursor = connection.cursor()
    cursor.execute(query)
    cursor.commit()


def getdata(query):
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.commit()
    result_set = [AttrDict({column[0]:res[i] for i,column in enumerate(cursor.description)}) for res in results]
    return result_set



