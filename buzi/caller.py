from redis import StrictRedis
import uuid
import time
import json

redis_conn = StrictRedis()

def call(name, *args, **kwargs):
    d = {
        'fn': name,
        'uuid': str(uuid.uuid4()),
        'args': args,
        'kwargs': kwargs
    }
    redis_conn.rpush('fn_%s' % name, json.dumps(d))

    while True:
        ret = redis_conn.get('fn_result_%s' % d['uuid'])
        if ret:
            return ret
        time.sleep(0.10)
