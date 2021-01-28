'''
'''
# ====== imports block ================================== #
from users import User


# ====== class declaration ============================== #
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


# ====== end of code ==================================== #
