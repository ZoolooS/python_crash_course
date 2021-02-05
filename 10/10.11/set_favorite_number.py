'''

'''
# ====== imports block ================================== #
import sys, os
import json


# ====== function declaration =========================== #
def write_to_file(path, content):
    try:
        with open(path, 'w', encoding="utf-8") as f:
            json.dump(content, f)
    except FileNotFoundError:
        print('К сожалению, не удалось открыть файл.')


def full_path(path, filename):
    return path + filename


# ====== main code ====================================== #
path = os.path.dirname(sys.argv[0]) + '/'
filename = 'fav_num.json'

fn = input('Укажите ваше любимое число: ')

write_to_file(full_path(path, filename), fn)


# ====== end of code ==================================== #
