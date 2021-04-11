
from Registration_new.registration import Registration
from Authorization_new.authorization import Authorization

class Menu():

    def menu(self):
        while True:
            choise = int(input("МЕНЮ""\n""1. Авторизация""\n"
                               "2. Регистрация""\n"
                               "3. Выход""\n"))

            if choise == 2:
                Registration().registration()


            if choise == 1:
                Authorization().authorization()




            if choise == 3:
                break


Menu().menu()



