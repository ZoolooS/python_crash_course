'''
'''
# ====== imports block ================================== #
from admins import Admin, Privileges

# ====== class declaration ============================== #


# ====== main code ====================================== #
user01 = Admin('Ilya', 'Popov', 'zooloos', 'qwerty', '+7-999-277-84-03', 'N/A')
# user02 = User('Kesha', 'Vorobey', 'Vorkesh', '12356', '+7-300-359-65-13', 'Не пою!')
# user03 = User('Stepan', 'Kaldera', 'goodone', 'asdfg', '+7-600-126-78-95', 'Щас спою!')

user01.privileges.show_privileges()

# ====== end of code ==================================== #
