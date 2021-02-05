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
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# ====== imports block ================================== #


# ====== function declaration =========================== #


# ====== main code ====================================== #
user01 = User('Ilya', 'Popov', 'zooloos', 'qwerty', '+7-999-277-84-03', 'N/A')
# user02 = User('Kesha', 'Vorobey', 'Vorkesh', '12356', '+7-300-359-65-13', 'Не пою!')
# user03 = User('Stepan', 'Kaldera', 'goodone', 'asdfg', '+7-600-126-78-95', 'Щас спою!')

print(user01.login_attempts)

user01.increment_login_attempts()
user01.increment_login_attempts()
user01.increment_login_attempts()
user01.increment_login_attempts()

print(user01.login_attempts)

user01.reset_login_attempts()

print(user01.login_attempts)

# ====== end of code ==================================== #
