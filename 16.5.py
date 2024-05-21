import sys

def check_arguments(arguments):
    if len(arguments) < 2:
        return False
    return True

def read_file(filename, options):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

            if '--sort' in options:
                lines.sort()

            if '--num' in options:
                lines = [f"{i} {line}" for i, line in enumerate(lines)]

            for line in lines:
                print(line.strip())

            if '--count' in options:
                print(f"rows count: {len(lines)}")

    except FileNotFoundError:
        print("ERROR")

if __name__ == "__main__":
    arguments = sys.argv[1:]

    if not check_arguments(arguments):
        print("ERROR: Missing filename argument")
    else:
        filename = arguments[-1]
        options = set(arguments[:-1])

        read_file(filename, options)