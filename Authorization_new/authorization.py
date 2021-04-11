
from statistics import mean
from Sql import DataBase
from Authorization_new.menu_student import Menu_student
from Authorization_new.menu_teacher import Menu_teacher

class Authorization:

    def authorization(self):

        log = input('Login: ')
        pas = input('Password: ')

        user = DataBase().getUser(log)

        if user != None and user['Password'] == pas:
            print(f"Вы вошли как {user['Status']}")
        else:
            print('Вы не зашли')

        while True:
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
                    break

            if user['Status'] == 'Teacher':
                menu_teacher = Menu_teacher().menu()
                if menu_teacher == 1:
                    change_kurs = DataBase().change_kurs()
                    for i in change_kurs:
                        print(i)
                    id = input("Введите id студента: ")
                    get_id = DataBase().get_id(id)
                    print(get_id)
                    kurs = input("Измените курс: ")
                    DataBase().add_Kurs(kurs,id)


                elif menu_teacher == 2:
                    change_marks = DataBase().change_kurs()
                    for i in change_marks:
                        print(i)
                    id = input("Введите id студента: ")
                    marks = DataBase().check_marks(id)
                    print(f"Математика: {marks['Mатематика']} \nФизика: {marks['Физика']} "
                            f" \nБиология: {marks['Биология']} \nИнформатика: {marks['Информатика']} "
                            f" \nРусский: {marks['Русский']}")


                    mathematics = input("Математика: ")
                    physics = input("Физика: ")
                    biology = input("Биология: ")
                    computer_science = input("Информатика ")
                    russian = input("Русский: ")
                    DataBase().change_marks(id,mathematics,physics,biology,computer_science,russian)


                elif menu_teacher == 3:
                    inform = DataBase().change_kurs()
                    for i in inform:
                        print(i)

                elif menu_teacher == 4:
                    break












