'''
'''


class Restaurant():
    '''
    '''

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'{self.restaurant_name.title()} is {self.cuisine_type}.')

    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is open!')

# ====== imports block ================================== #


# ====== function declaration =========================== #


# ====== main code ====================================== #
rest01 = Restaurant('Lavender', 'anticafe')
rest02 = Restaurant('Mac', 'fastfood')
rest03 = Restaurant('Izbushka', 'russian food')

rest01.describe_restaurant()
rest02.describe_restaurant()
rest03.describe_restaurant()


# ====== end of code ==================================== #
