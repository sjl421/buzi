buzi
===========================================
buzi is a simple mikro service architecture

    from buzi.deco import service, services

    @service("foo")
    def foo(a, b):
        return a + b


    if __name__ == '__main__':
        from buzi.runner import run
        run()


and the calling code

    from buzi.caller import call
    print call("foo", 2, 4)


its in early stage so api and all is subject to change

install
----------------
- git clone git@github.com:ybrs/buzi.git
- python setup.py develop

