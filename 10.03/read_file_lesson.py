'''
'''
# ====== imports block ================================== #
import sys, os

# ====== function declaration =========================== #


# ====== main code ====================================== #
path = os.path.dirname(sys.argv[0]) + '/' + 'guest.txt'

name = input('What is you name? -> ')

with open(path, 'w') as f:
    f.write(name)


# ====== end of code ==================================== #
