'''
'''
# ====== imports block ================================== #
from restaurant import Restaurant


# ====== class declaration ============================== #
class IceCreamStand(Restaurant):
    '''
    '''

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def get_flavors(self, *flavors):
        self.flavors = flavors

    def print_flavors(self):
        if self.flavors == []:
            print('Sorry, there is no any icecream yet.')
        else:
            print('We have some flavors of icecream:')
            print(*self.flavors, sep='\n')
            print('Chouse what you want.')


# ====== main code ====================================== #
restaurant = Restaurant('Lavender', 'anticafe')

restaurant.describe_restaurant()
restaurant.open_restaurant()

# ====== end of code ==================================== #
