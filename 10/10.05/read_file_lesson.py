'''
'''
# ====== imports block ================================== #
import sys, os

# ====== function declaration =========================== #


# ====== main code ====================================== #
path = os.path.dirname(sys.argv[0]) + '/' + 'reasons.txt'

print('Hello there!')
print('Why do you love coding?')
print('Enter your reason or "end".')

while True:
    reason = input('Your reason -> ')
    if reason == "end":
        print('Thanks! Cya.')
        break
    else:
        with open(path, 'a') as f:
            f.write(f'{reason}\n')


# ====== end of code ==================================== #
