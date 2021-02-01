'''
'''
# ====== imports block ================================== #
import sys, os

# ====== function declaration =========================== #


# ====== main code ====================================== #
path = os.path.dirname(sys.argv[0]) + '/learning_python.txt'

with open(path) as f:
    print(f.read())

print('===========')

with open(path) as f:
    for line in f:
        print(line.strip())

print('===========')

with open(path) as f:
    text_to_list = f.readlines()

for line in text_to_list:
    print(line.strip())

# ====== end of code ==================================== #
