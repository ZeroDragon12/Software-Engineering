# 9, 10
import pytest


def count_chars(s):
    if not isinstance(s, str):
        raise TypeError('Input should be a string')

    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


@pytest.mark.parametrize('input_str, expected', [
    ('', {}),
    ('a', {'a': 1}),
    ('aaa', {'a': 3}),
    ('hello', {'h': 1, 'e': 1, 'l': 2, 'o': 1}),
    ('madam', {'m': 2, 'a': 2, 'd': 1}),
])
def test_count_chars(input_str, expected):
    assert count_chars(input_str) == expected


def test_not_string_type_error():
    with pytest.raises(TypeError):
        count_chars(123)
