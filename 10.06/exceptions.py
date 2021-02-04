'''

'''
# ====== imports block ================================== #


# ====== function declaration =========================== #
def sum_with_check():
    try:
        n, m = int(input('Enter first number: ')), int(input('Enter second number: '))
    except ValueError:
        print('Well, you definetly insert not number...')
    else:
        print(f'The sum of {n} and {m} is {n + m}.')


# ====== main code ====================================== #
sum_with_check()

# ====== end of code ==================================== #
