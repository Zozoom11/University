
from statistics import mean
from Sql import DataBase
from Authorization_new.menu_student import Menu_student

class Authorization:

    def authorization(self):

        while True:
            log = input('Login: ')
            pas = input('Password: ')

            user = DataBase().getUser(log)

            if user != None and user['Password'] == pas:
                print('Вы вошли как ' + user['Status'])
            else:
                print('Вы не зашли')

            if user['Status'] == 'Student':
                menu_student = Menu_student().menu()
                if menu_student == 1:
                    mark = DataBase().check_mark(log)
                    print(f"Математика: {mark['Mатематика']} \nФизика: {mark['Физика']} "
                          f" \nБиология: {mark['Биология']} \nИнформатика: {mark['Информатика']} "
                          f" \nРусский: {mark['Русский']}")

                elif menu_student == 2:
                    mark = DataBase().check_mark(log)
                    kurs = DataBase().check_kurs(log)
                    initials = DataBase().check_initials(log)
                    print(initials['ФИО'])
                    print(f"Cредний балл: {mean(mark[i] for i in mark)}")
                    print(f"Курс: {kurs['Курс']}")

                elif menu_student == 3:
                    # тут пока ничего нету!!!!




            #elif user['Status'] == 'Teacher':
                #login_teacher = log
                #return login_teacher





