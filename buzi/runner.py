import redis
import time
import json
import logging
from buzi.conn import get_connection

logger = logging.getLogger(__name__)

def run(services=None):
    if services is None:
        from buzi.deco import services

    redis_conn = get_connection()
    chans = []
    for k, v in services.iteritems():
        chans.append('fn_%s' % k)

    while True:
        t = redis_conn.blpop(*chans)
        queue_name, value = t
        t1 = time.time()
        logger.debug("received - %s", value)
        v = json.loads(value)
        ret = services[v['fn']]['fn'](*v['args'], **v['kwargs'])
        redis_conn.lpush('fn_result_%s' % v['uuid'], json.dumps({'result':ret}))
        logger.debug("returned - %s %s msecs", v['fn'], (time.time() - t1))

if __name__ == '__main__':
    run({})