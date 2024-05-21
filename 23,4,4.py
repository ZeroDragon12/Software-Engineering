# 7
import unittest


def reverse(s):
    return s[::-1]


class TestReverse(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse(''), '')

    def test_one_symbol(self):
        self.assertEqual(reverse('a'), 'a')

    def test_palindrome(self):
        self.assertEqual(reverse('madam'), 'madam')

    def test_not_palindrome(self):
        self.assertEqual(reverse('hello'), 'olleh')

    def test_not_string_not_iterable(self):
        with self.assertRaises(TypeError):
            reverse(123)

    def test_not_string_iterable(self):
        self.assertEqual(reverse([1, 2, 3]), [3, 2, 1])

if __name__ == '__main__':
    unittest.main()
