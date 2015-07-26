import sys
import buzi.runner

class TransportHttp(object):
    def __init__(self, port, host=None):
        self.port = port



transports = {
    'http': TransportHttp
}

def run_obj(obj):
    for k,v in obj.items():
        t = v['transport'].pop('method')
        transporter = transports[t]
        transporter(**v['transport'])

def run_yaml(yml_file):
    import yaml
    with open(yml_file, 'r') as stream:
        config = yaml.load(stream)
        for o in config:
            run_obj(o)

def run(module_name):
    if module_name.endswith('.yml'):
        run_yaml(module_name)
    else:
        import sys, os
        sys.path.append(os.getcwd())
        mdl = __import__(module_name, globals=globals(), level=-1)
        buzi.runner.run()

commands = {
    'run': run
}

def main():
    if len(sys.argv) < 0:
        print("Usage: buzi run somemodule")
        return

    cmd = sys.argv[1]
    if not cmd in commands:
        print("Unknown command")
        return

    commands[cmd](*sys.argv[2:])
