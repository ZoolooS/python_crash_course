'''

'''
# ====== imports block ================================== #
import unittest
from city_functions import city_name_format


# ====== function declaration =========================== #
class CityTestCases(unittest.TestCase):
    """..."""
    def test_city_country(self):
        """..."""
        formated_city_name = city_name_format('russia', 'psKov')
        self.assertEqual(formated_city_name, '"Pskov, Russia"')
    def test_city_country_population(self):
        """..."""
        formated_city_name = city_name_format('russia', 'psKov', '1300000')
        self.assertEqual(formated_city_name, '"Pskov, Russia - population 1300000"')


# ====== main code ====================================== #
if __name__ == '__main__':
    unittest.main()

# ====== end of code ==================================== #
