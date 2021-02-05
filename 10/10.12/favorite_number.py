'''

'''
# ====== imports block ================================== #
import sys, os
import json


# ====== function declaration =========================== #
def full_path(path, filename):
    return path + filename


def write_to_file(path, content):
    try:
        with open(path, 'w', encoding="utf-8") as f:
            json.dump(content, f)
    except FileNotFoundError:
        print('К сожалению, не удалось открыть файл.')


def read_from_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            content = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return content


def fav_num(path, filename):
    if not read_from_file(full_path(path, filename)):
        fn = input('Укажите ваше любимое число: ')
        write_to_file(full_path(path, filename), fn)
    else:
        print(f"Hey, I know your favorite number! It's {read_from_file(full_path(path, filename))}.")


# ====== main code ====================================== #
path = os.path.dirname(sys.argv[0]) + '\\'
filename = 'fav_num.json'

print('Hello there!')
fav_num(path, filename)

# ====== end of code ==================================== #
