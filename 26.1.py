class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass

class DefaultList(list):
    def __init__(self, default):
        self.default = default
        super().__init__()

    def __getitem__(self, i):
        try:
            return super().__getitem__(i)
        except IndexError:
            return self.default


def check_password(password):
    try:
        assert len(password) > 8, "Password length should be at least 9 characters"
        assert any(char.isupper() for char in password) and any(char.islower() for char in password), "Password should contain both uppercase and lowercase letters"
        assert any(char.isdigit() for char in password), "Password should contain at least one digit"

        invalid_combinations = ['123', '234', '345', '456', '567', '678', '789',
                                'qwe', 'wer', 'ert', 'rty', 'tyu', 'yui', 'uio', 'iop',
                                'asd', 'sdf', 'dfg', 'fgh', 'ghj', 'hjk', 'jkl',
                                'zxc', 'xcv', 'cvb', 'vbn', 'bnm',
                                'йцу', 'цук', 'уке', 'кен', 'енг', 'нгш', 'гшщ', 'шщз', 'щзх', 'зхъ',
                                'фыв', 'выа', 'вап', 'апр', 'про', 'рол', 'олд', 'лдж', 'джэ',
                                'ячс', 'чсм', 'сми', 'мит', 'ить', 'тьб', 'ьбю']
        for comb in invalid_combinations:
            assert comb not in password.lower() and comb[::-1] not in password.lower(), "Password should not contain invalid sequences"

    except LengthError as e:
        raise e
    except LetterError as e:
        raise e
    except DigitError as e:
        raise e
    except SequenceError as e:
        raise e
    except AssertionError as e:
        raise PasswordError(str(e))

    return "ok"


while True:
    password = input("Введите пароль: ")

    try:
        if password.lower() == "ctrl+break":
            raise KeyboardInterrupt
        result = check_password(password)
        print(result)
        break
    except KeyboardInterrupt:
        print("Bye-Bye")
        exit()
    except PasswordError as e:
        print("Error:", e)