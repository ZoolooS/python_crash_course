'''
'''


class User():
    '''
    '''

    def __init__(self, first_name, last_name, login, password, phone, about):
        self.first_name = first_name
        self.last_name = last_name
        self.login = login
        self.password = password
        self.phone = phone
        self.about = about

    def describe_user(self):
        print(
                f'{self.first_name.title()} {self.last_name.title()} '
                f'has login - {self.login}.\n'
                f'You can call by {self.phone}.\n'
                f'{self.first_name.title()} wrote about him/her-self '
                f'"{self.about}"'
        )

    def greet_user(self):
        print(f'Hello, {self.first_name.title()} {self.last_name.title()}!')

# ====== imports block ================================== #


# ====== function declaration =========================== #


# ====== main code ====================================== #
user01 = User('Ilya', 'Popov', 'zooloos', 'qwerty', '+7-999-277-84-03', 'N/A')
user02 = User('Kesha', 'Vorobey', 'Vorkesh', '12356', '+7-300-359-65-13', 'Не пою!')
user03 = User('Stepan', 'Kaldera', 'goodone', 'asdfg', '+7-600-126-78-95', 'Щас спою!')

user01.greet_user()
user01.describe_user()
print('============')
user02.greet_user()
user02.describe_user()
print('============')
user03.greet_user()
user03.describe_user()
print('============')


# ====== end of code ==================================== #
