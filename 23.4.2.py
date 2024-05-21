# 3, 4
def is_correct_mobile_phone_number_ru(number):
    number = number.replace(" ", "").replace("-", "").replace("(", "").replace(")", "")

    if not number.startswith("8") and not number.startswith("+7"):
        return False
    if len(number) != 11 and len(number) != 12:
        return False
    if len(number) == 12:
        operator_code = number[2:5]
    else:
        operator_code = number[1:4]

    if not operator_code.isdigit() or len(operator_code) != 3:
        return False
    for char in number:
        if len(number) == 12:
            if char != '+':
                if not char.isdigit():
                    return False
        else:
            if not char.isdigit():
                return False
    if number.startswith("8") and len(number) == 12:
        return False
    return True


def te_is_correct_mobile_phone_number_ru():
    test_cases = [
        ("89001234567", True),
        ("+79001234567", True),
        ("+7 (900) 123-45-67", True),
        ("8 900 123 45 67", True),
        ("8900123456", False),
        ("79001234567", False),
        ("+790012345678", False),
        ("89001234567a", False),
        ("8 900 123 45 67 8", False),
    ]

    for number, expected in test_cases:
        result = is_correct_mobile_phone_number_ru(number)
        if result == expected:
            print("YES")
        else:
            print("NO")


te_is_correct_mobile_phone_number_ru()
