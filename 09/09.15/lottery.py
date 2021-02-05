'''
'''
# ====== imports block ================================== #
from random import choice


# ====== class declaration ============================== #
class Lottery():
    '''
    '''

    def __init__(self):
        self.alphabet = (
                '0', '1', '2', '3', '4', 
                '5', '6', '7', '8', '9', 
                'A', 'B', 'C', 'D', 'E'
        )

    def lottery_roll(self):
        return [choice(self.alphabet) for i in range(4)]


# ====== end of code ==================================== #
