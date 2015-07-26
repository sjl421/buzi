import aioredis
import asyncio
import logging
import uuid
import json

logger = logging.getLogger(__name__)

class Buzi(object):

    @asyncio.coroutine
    def call(self, name, *args, **kwargs):
        loop = asyncio.get_event_loop()
        self.client = yield from aioredis.create_redis(
        ('localhost', 6379), loop=loop)
        d = {
            'fn': name,
            'uuid': str(uuid.uuid4()),
            'args': args,
            'kwargs': kwargs
        }
        yield from self.client.rpush('fn_%s' % name, json.dumps(d))
        ret = yield from self.client.blpop('fn_result_%s' %d['uuid'], 0)
        ret_val = ret[1].decode('utf-8')
        result = json.loads(ret_val)
        if 'error' in result:
            raise Exception(result['error'])
        print('result', result.get('result'))
        return result['result']

