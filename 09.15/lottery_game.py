'''
'''
# ====== imports block ================================== #
from lottery import Lottery


# ====== function declaration =========================== #
def is_ticket_lucky(ticket, combination):
    if sorted(ticket) == sorted(combination):
        return True
    else:
        False


def roll_while_win():
    count = 0
    while not is_ticket_lucky(ticket, game.lottery_roll()):
        count += 1
    else:
        print(f'Yay! Your ticket was won from the {count} time.')


# ====== main code ====================================== #
game = Lottery()
ticket = game.lottery_roll()

roll_while_win()


# ====== end of code ==================================== #
