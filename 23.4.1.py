# 1, 2
def is_palindrome(data):
    if data.lower() == data.lower()[::-1]:
        return True
    else:
        return False


def te_is_palindrome():
    test_cases = [
        ("noon", True),
        ("step on no step", False),
        ("abcba", True),
        ("racecar", True),
        ("no", False),
        ("hello world", False),
    ]
    for input_str, expected_result in test_cases:
        result = is_palindrome(input_str)
        if result != expected_result:
            return "NO"
    return "YES"


def main():
    data = input("Введите строку: ")
    if is_palindrome(data):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    main()
    print(te_is_palindrome())
