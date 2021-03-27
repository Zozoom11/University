
from Sql import DataBase
from menu import Menu

class Reqistration(Menu):

    def reqistration(self):

        choise = Menu.menu(self)

        if choise == 2:
            name = input('Input Name: ')
            log = input('Input Login: ')
            pas = input('Input Password: ')
            status = input('Input Status("Student" or "Teacher": ')

            pas = pas.replace('1', '222').replace('7', '888')

            DataBase().addUser(name, log, pas, status)
            return name, log, pas, status



Reqistration().reqistration()





    