from functools import wraps
import sys
import inspect
import os.path

services = {}

class service(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, fn):

        assert inspect.isfunction(fn)

        mdl = inspect.getmodule(fn)
        file = os.path.realpath(mdl.__file__)

        services[self.name] = {
            'fn': fn,
            'path': (file, fn.__name__)
        }

        @wraps(fn)
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper


