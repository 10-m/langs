#!env python3
# -*- coding: utf-8 -*-

import json
from datetime import datetime

class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)

def dumps(obj):
    return json.dumps(obj, cls=JSONDateTimeEncoder)

print(dumps({'time': datetime.now()}))

time_str = '2012/01/01 12:32:11'
dt = datetime.strptime(time_str, '%Y/%m/%d %H:%M:%S')
print(dt)
