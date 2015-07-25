import redis
import json

def run(services=None):
    if services is None:
        from buzi.deco import services

    redis_conn = redis.StrictRedis()
    chans = []
    for k, v in services.iteritems():
        chans.append('fn_%s' % k)

    while True:
        t = redis_conn.blpop(*chans)
        queue_name, value = t
        v = json.loads(value)
        ret = services[v['fn']]['fn'](*v['args'], **v['kwargs'])
        redis_conn.set('fn_result_%s' % v['uuid'], json.dumps(ret))


if __name__ == '__main__':
    run({})