import sys

def parse_arguments(arguments):
    parsed_args = {}
    for arg in arguments:
        key_value = arg.split('=')
        if len(key_value) == 2:
            key, value = key_value
            parsed_args[key] = value
        else:
            print("Invalid argument format:", arg)
    return parsed_args

def print_arguments(arguments, sort=False):
    if sort:
        arguments = sorted(arguments.items())
    for key, value in arguments:
        print("Key:", key, "Value:", value)

def main():
    sort = False
    if '--sort' in sys.argv:
        sort = True
        sys.argv.remove('--sort')

    arguments = parse_arguments(sys.argv[1:])

    print_arguments(arguments, sort)

if __name__ == "__main__":
    main()