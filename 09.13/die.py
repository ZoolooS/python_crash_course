'''
'''
# ====== imports block ================================== #
from random import randint


# ====== class declaration ============================== #
class Die():
    '''
    '''

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)


# ====== end of code ==================================== #
