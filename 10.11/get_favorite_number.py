'''

'''
# ====== imports block ================================== #
import sys, os
import json


# ====== function declaration =========================== #
def read_from_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            content = json.load(f)
    except FileNotFoundError:
        print('К сожалению, не удалось открыть файл.')
    else:
        return content


def full_path(path, filename):
    return path + filename


# ====== main code ====================================== #
path = os.path.dirname(sys.argv[0]) + '/'
filename = 'fav_num.json'

print(f"Hey, I know your favorite number! It's {read_from_file(full_path(path, filename))}.")


# ====== end of code ==================================== #
