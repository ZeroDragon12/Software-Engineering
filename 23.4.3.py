# 5, 6
import string


def strip_punctuation_ru(data):
    words = data.split()
    new_words = ''
    prob = []
    for word in words:
        new_word = word.translate(str.maketrans('', '', string.punctuation))
        new_words += new_word + ' '
    new_words = new_words.replace('  ', ' ')
    if new_words != '':
        c = len(new_words)-1
        new_words = new_words[:c]
    return new_words


def simple_text():
    text = 'Привет, мир! Это - тестовая строка. Как дела?'
    expected = 'Привет мир Это тестовая строка Как дела'
    result = strip_punctuation_ru(text)
    return result == expected


def complex_text():
    text = 'Привет, мир! Это - тестовая строка. Как дела? А вот ещё предложение.'
    expected = 'Привет мир Это тестовая строка Как дела А вот ещё предложение'
    result = strip_punctuation_ru(text)
    return result == expected


def empty_string():
    text = ''
    expected = ''
    result = strip_punctuation_ru(text)
    return result == expected


if __name__ == '__main__':
    print(simple_text())
    print(complex_text())
    print(empty_string())
    print('Все тесты пройдены.')