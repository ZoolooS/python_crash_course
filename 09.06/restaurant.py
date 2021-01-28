'''
'''
# ====== imports block ================================== #


# ====== class declaration =========================== #
class Restaurant():
    '''
    '''

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type)

    def open_restaurant(self):
        print(f'{self.restaurant_name.title()} is open!')

    def increment_number_served(self, served_per_day):
        self.number_served += served_per_day


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
restaurant = IceCreamStand('Lavender', 'anticafe')

restaurant.print_flavors()
restaurant.get_flavors('vanilla', 'choco', 'pistachio')
restaurant.print_flavors()

# ====== end of code ==================================== #
