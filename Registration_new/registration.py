
from Sql import DataBase

class Registration:

    def registration(self):

        while True:
            name = input('Input Name: ')
            log = input('Input Login: ')
            pas = input('Input Password: ')
            status = input('Input Status("Student" or "Teacher"): ')

            check = DataBase().check_login()

            if log in check:
                print('Логин занят')
            else:
                pas = pas.replace('1', '222').replace('7', '888')
                DataBase().addUser(name, log, pas, status)
                return name, log, pas, status












    