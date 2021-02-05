'''
'''
# ====== imports block ================================== #
import sys, os

# ====== function declaration =========================== #


# ====== main code ====================================== #
path = os.path.dirname(sys.argv[0]) + '/' + 'guest_book.txt'

print('Hello there! You need to register.')
print('Enter your name or "end".')

while True:
    name = input('Your name -> ')
    if name == "end":
        print('Cya!')
        break
    else:
        print(f'Hello, {name}!')
        with open(path, 'a') as f:
            f.write(f'New user: {name}\n')


# ====== end of code ==================================== #
