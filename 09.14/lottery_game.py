'''
'''
# ====== imports block ================================== #
from lottery import Lottery

# ====== class declaration ============================== #


# ====== main code ====================================== #
game = Lottery()
print("And winner's numbers/letters:")
print(*game.lottery_roll(), sep=', ')

# ====== end of code ==================================== #
