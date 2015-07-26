"""
you can run this with:

    buzi run examples.example

"""
from buzi.deco import service
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("hello")

@service("foo")
def foo(a, b):
    return a + b

@service("multiply")
def bar(a, b, c):
    return a * b * c

if __name__ == '__main__':
    from buzi.runner import run
    run()