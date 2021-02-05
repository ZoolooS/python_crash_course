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


# ====== end of code ==================================== #
