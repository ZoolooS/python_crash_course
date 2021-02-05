'''

'''
# ====== imports block ================================== #
import sys, os


# ====== function declaration =========================== #
def open_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            content = f.readlines()
    except FileNotFoundError:
        pass  # print('К сожалению, файл не найден.')
    else:
        return [name.rstrip() for name in content]


def print_list(path):
    try:
        print(*open_file(path), sep=', ')
    except TypeError:
        pass  # print('на входе должен быть список для корректной работы.')


# ====== main code ====================================== #
path = os.path.dirname(sys.argv[0]) + '/'
path_cats = f'{path}cats.txt'
path_dogs = f'{path}dogs.txt'

print('Кошки:')
print_list(path_cats)
print('Собаки:')
print_list(path_dogs)

# ====== end of code ==================================== #