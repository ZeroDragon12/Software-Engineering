def is_palindrome(data):
    return data == data[::-1]


def is_palindrome_test():
    test_cases = ["radar", "level", "deified", "noon", "hello", "12321", "*-*", "&yhds9&"]
    expected_results = [True, True, True, True, False, True, True, False]

    for i, test_case in enumerate(test_cases):
        result = is_palindrome(test_case)
        if result == expected_results[i]:
            continue
        else:
            print("NO")
            return
    print("YES")


is_palindrome_test()
