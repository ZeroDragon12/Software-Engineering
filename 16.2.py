import sys

def calculate_sum(args):
    total_sum = 0
    sign = 1

    for arg in args:
        try:
            num = int(arg)
            total_sum += sign * num
            sign *= -1
        except ValueError:
            continue

    return total_sum

def main():
    if len(sys.argv) < 2:
        print("NO PARAMS")
        return

    print(calculate_sum(sys.argv[1:]))

if __name__ == "__main__":
    main()