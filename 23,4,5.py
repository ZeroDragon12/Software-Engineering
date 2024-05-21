import pytest


def reverse(s):
    return s[::-1]


def test_empty_string():
    assert reverse('') == ''


def test_one_symbol():
    assert reverse('a') == 'a'


def test_palindrome():
    assert reverse('madam') == 'madam'


def test_not_palindrome():
    assert reverse('hello') == 'olleh'


def test_not_string_not_iterable():
    with pytest.raises(TypeError):
        reverse(123)


def test_not_string_iterable():
    assert reverse([1, 2, 3]) == [3, 2, 1]
