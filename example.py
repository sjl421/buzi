from buzi.deco import service, services

@service("foo")
def foo(a, b):
    return a + b


if __name__ == '__main__':
    from buzi.runner import run
    run()