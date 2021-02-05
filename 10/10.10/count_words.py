'''

'''
# ====== imports block ================================== #
import sys, os


# ====== function declaration =========================== #
def open_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print('К сожалению, файл не найден.')
    else:
        return content


def count_words(title, text, word):
    print(f'В файле {title} {text.lower().count(word)} слов "{word}".')


def full_path(path, title):
    return path + title


# ====== main code ====================================== #
path = os.path.dirname(sys.argv[0]) + '/'
title01 = 'Peter_Pan.txt'
title02 = "Grimms'_Fairy_Tales.txt"
word = input('Введите слово которое будем искать: ')

count_words(title01, open_file(full_path(path, title01)), word)
count_words(title02, open_file(full_path(path, title02)), word)

# ====== end of code ==================================== #
