
from Sql import DataBase


class Authorization:

    def authorization(self):

        log = input('Login: ')
        pas = input('Password: ')

        user = DataBase().getUser(log)


        if user != None and user['Password'] == pas:

            print('вы вошли как ' + user['Status'])
        else:
            print('вы не зашли')





