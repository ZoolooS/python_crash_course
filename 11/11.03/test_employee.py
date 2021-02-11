'''

'''
# ====== imports block ================================== #
import unittest
from employee import Employee


# ====== function declaration =========================== #
class TestEmployee(unittest.TestCase):
    """Тесты для класса Employee"""

    def setUp(self):
        """
            Создание экземпляра объекта Employee
            и входных данных для всех тестовых методов.
        """
        name = 'john'
        surname = 'Smith'
        annual_salary = 93500
        self.my_employee = Employee(name, surname, annual_salary)
        self.annual_salary_raise = 7000

    def test_give_default_raise(self):
        """Проверяет, что данные с дефолтным повышением отображаются верно."""
        start_annual_salary = self.my_employee.annual_salary
        self.my_employee.give_raise()
        end_annual_salary = self.my_employee.annual_salary
        self.assertIn(str(start_annual_salary
                          + self.my_employee.annual_salary_raise),
                      str(end_annual_salary))

    def test_give_custom_raise(self):
        """Проверяет, что данные с кастомным повышением отображаются верно."""
        start_annual_salary = self.my_employee.annual_salary
        self.my_employee.give_raise(self.annual_salary_raise)
        end_annual_salary = self.my_employee.annual_salary
        self.assertIn(str(start_annual_salary
                          + self.annual_salary_raise),
                      str(end_annual_salary))


# ====== main code ====================================== #
if __name__ == "__main__":
    unittest.main()

# ====== end of code ==================================== #
