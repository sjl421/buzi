import tornadoredis
import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.gen
import logging
import uuid
import json

logger = logging.getLogger(__name__)

class Buzi(object):

    def __init__(self, loop=None):
        self.loop = loop

        if not loop:
            self.loop = tornado.ioloop.IOLoop.instance()

        self.client = tornadoredis.Client()

    @tornado.gen.engine
    def call_(self, name, *args, **kwargs):
        callback = kwargs.pop('callback')
        d = {
            'fn': name,
            'uuid': str(uuid.uuid4()),
            'args': args,
            'kwargs': kwargs
        }
        pushed = yield tornado.gen.Task(self.client.rpush, 'fn_%s' % name, json.dumps(d))

        ret = yield tornado.gen.Task(self.client.blpop, 'fn_result_%s' % d['uuid'], 0)
        ret_val = None
        for k, v in ret.iteritems():
            ret_val = v

        callback(json.loads(ret_val))

    def call(self, *args, **kwargs):
        try:
            return tornado.gen.Task(Buzi().call_, *args, **kwargs)
        except Exception as e:
            logger.exception("exception while sending task")
            raise