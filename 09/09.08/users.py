'''
'''
# ====== imports block ================================== #


# ====== class declaration ============================== #
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


class Admin(User):
    '''
    '''

    def __init__(self, first_name, last_name, login, password, phone, about):
        super().__init__(first_name, last_name, login, password, phone, about)
        self.privileges = Privileges()


class Privileges():
    '''
    '''

    def __init__(self):
        self.privileges = [
                'Allowed add users',
                'Allowed delete users',
                'Allowed change users',
                'Allowed ban users',
        ]

    def show_privileges(self):
        print("Admin's rights:")
        print(*self.privileges, sep='\n')


# ====== main code ====================================== #
user01 = Admin('Ilya', 'Popov', 'zooloos', 'qwerty', '+7-999-277-84-03', 'N/A')
# user02 = User('Kesha', 'Vorobey', 'Vorkesh', '12356', '+7-300-359-65-13', 'Не пою!')
# user03 = User('Stepan', 'Kaldera', 'goodone', 'asdfg', '+7-600-126-78-95', 'Щас спою!')

user01.privileges.show_privileges()

# ====== end of code ==================================== #
