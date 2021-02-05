'''

'''
# ====== imports block ================================== #


# ====== function declaration =========================== #
def is_number(value):
    try:
        n = int(value)
    except ValueError:
        print('Well, you definetly insert not a number...')
    else:
        return n


def sum_with_check():
    n, m = 'zero', 'zero'
    while not str(n).isdecimal():
        n = is_number(input('Enter first number: '))
    while not str(m).isdecimal():
        m = is_number(input('Enter second number: '))

    print(f'The sum of {n} and {m} is {n + m}.')


# ====== main code ====================================== #
sum_with_check()

# ====== end of code ==================================== #
