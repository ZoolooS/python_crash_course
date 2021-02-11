'''

'''
# ====== imports block ================================== #


# ====== function declaration =========================== #
class Employee():
    """Employee description."""

    def __init__(self, name, surname, annual_salary):
        """
            Получает имя, фамилию и ежегодный оклад.
            Сохраняет полученные данные в аттрибутах.
        """
        self.name = name
        self.surname = surname
        self.annual_salary = annual_salary

    def give_raise(self, annual_salary_raise=5000):
        self.annual_salary_raise = annual_salary_raise
        self.annual_salary += self.annual_salary_raise


# ====== main code ====================================== #


# ====== end of code ==================================== #
