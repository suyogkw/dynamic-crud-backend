from attrdict import AttrDict
import datetime

def get_sqlquery(queryobject, **formatters):
    query = queryobject.query
    params = tuple(x.format(**formatters) for x in queryobject.params)

    return query, params

def jsonconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()[:-3]
    if isinstance(o, AttrDict):
        return dict(o)