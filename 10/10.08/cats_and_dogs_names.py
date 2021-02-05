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
        print('К сожалению, файл не найден.')
    else:
        return [name.rstrip() for name in content]


# ====== main code ====================================== #
path = os.path.dirname(sys.argv[0]) + '/'
path_cats = f'{path}cats.txt'
path_dogs = f'{path}dogs.txt'

print('Кошки:')
print(*open_file(path_cats), sep=', ')
print('Собаки:')
print(*open_file(path_dogs), sep=', ')

# ====== end of code ==================================== #