import sys


def main():
    if len(sys.argv) != 3:
        print(0)
        return

    try:
        arg1 = int(sys.argv[1])
        arg2 = int(sys.argv[2])
    except ValueError:
        print(0)
        return

    print(arg1 + arg2)


if __name__ == "__main__":
    main()
