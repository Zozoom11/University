
from Registration_new.registration import Registration
from Authorization_new.authorization import Authorization

class Menu():

    def menu(self):
        while True:
            choise = int(input("МЕНЮ""\n""1. Authorization""\n"
                               "2. Reqistration""\n"
                               "3. close""\n"))

            if choise == 2:
                return Registration().registration()

            if choise == 1:
                return Authorization().authorization()






