import sys

def main():
    if len(sys.argv) != 4:
        print("Error: Incorrect number of arguments")
        return

    try:
        arg1 = float(sys.argv[1])
        arg2 = float(sys.argv[2])
    except ValueError:
        print("Error: Invalid input")
        return

    operator = sys.argv[3]
    if operator == '+':
        print(arg1 + arg2)
    elif operator == '-':
        print(arg1 - arg2)
    elif operator == '*':
        print(arg1 * arg2)
    elif operator == '/':
        if arg2 == 0:
            print("Error: Division by zero")
        else:
            print(arg1 / arg2)
    elif operator == '^':
        print(arg1 ** arg2)
    else:
        print("Error: Invalid operator")

if __name__ == "__main__":
    main()