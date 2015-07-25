import uuid
import time
import json
from buzi.conn import get_connection

redis_conn = get_connection()


class Buzi(object):

    def __init__(self):
        pass

    def call(self, name, *args, **kwargs):
        d = {
            'fn': name,
            'uuid': str(uuid.uuid4()),
            'args': args,
            'kwargs': kwargs
        }
        redis_conn.rpush('fn_%s' % name, json.dumps(d))

        while True:
            ret = redis_conn.blpop('fn_result_%s' % d['uuid'])
            if ret:
                return json.loads(ret[1])
