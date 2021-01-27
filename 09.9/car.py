'''
'''
# ====== imports block ================================== #


# ====== class declaration ============================== #
class Car():
    '''
        Simple car model
    '''

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    '''
        Aspects, special for electric cars
    '''

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car dosn't need a gas tank.")


class Battery():
    '''
        Simple model of battery for electric cars.
    '''

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery.')

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f'This car can go about {range} miles on a full charge.')

    def upgrade_battery(self):
        if self.battery_size != 100:
            self.battery_size = 100


# ====== main code ====================================== #
car = ElectricCar('Tesla', 'Model 3', '2018')

car.battery.get_range()
car.battery.upgrade_battery()
car.battery.get_range()


# ====== end of code ==================================== #
