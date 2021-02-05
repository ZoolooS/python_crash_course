'''
'''


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

# ====== imports block ================================== #


# ====== function declaration =========================== #


# ====== main code ====================================== #
restaurant = Restaurant('Lavender', 'anticafe')

print(restaurant.number_served)
restaurant.number_served = 21
print(restaurant.number_served)
restaurant.increment_number_served(15)
print(restaurant.number_served)

# ====== end of code ==================================== #
