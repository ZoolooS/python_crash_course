'''

'''
# ====== imports block ================================== #
import sys, os
import json


# ====== function declaration =========================== #
def full_path(path, filename):
    return path + filename


def get_stored_name(path):
    """Получает хранимое имя пользователя, если оно существует."""
    try:
        with open(path) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username(path):
    """Запрашивает новое имя пользователя"""
    username = input("What's your name? -> ")
    with open(path, 'w') as f:
        json.dump(username, f)
    return username


def greet_user(path):
    """Приветствует пользователя по имени"""
    username = get_stored_name(path)
    if username:
        print('Hello, there.')
        is_cur_username = input(f'Are you {username}? (y/n) ')
        if is_cur_username == 'y':
            print(f"Wellcome back, {username}!")
        elif is_cur_username == 'n':
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
        else:
            print('Something wrong there..')
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")


# ====== main code ====================================== #
rel_path = os.path.dirname(sys.argv[0]) + '\\'
filename = 'username.json'
path = full_path(rel_path, filename)

greet_user(path)

# ====== end of code ==================================== #
