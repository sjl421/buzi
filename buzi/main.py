import sys
import buzi.runner

def run(module_name):
    mdl = __import__(module_name, globals=globals())
    buzi.runner.run()

commands = {
    'run': run
}

def main():
    if len(sys.argv) < 0:
        print("Usage: buzi run somemodule")
        return

    try:
        cmd = sys.argv[1]
        commands[cmd](*sys.argv[2:])
    except KeyError as e:
        print("Unknown command")