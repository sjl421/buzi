from buzi.deco import service, services
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("hello")

@service("foo")
def foo(a, b):
    return a + b


if __name__ == '__main__':
    from buzi.runner import run
    run()