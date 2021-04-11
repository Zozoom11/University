
import pymysql
from pymysql.cursors import DictCursor

class DataBase:
    def __init__(self):
        self.connection = self.connect()
        self.cursors = self.connection.cursor()

    def connect(self):
        connection = pymysql.connect(
            host='localhost',
            user='unomom',
            password='1234554321',
            database='unomom',
            charset='utf8mb4',
            cursorclass=DictCursor
        )
        return connection

    def addUser(self,name,login,password,status):
        sql = "INSERT INTO people (name,login,password,status) VALUES (%s, %s, %s, %s) "
        temp = [name,login,password,status]
        self.cursors.execute(sql,temp)
        self.connection.commit()
        if status == 'Student':
            sql = "INSERT INTO students (name,login) VALUES ( %s, %s ) "
            temp = [name,login]
            self.cursors.execute(sql, temp)
            self.connection.commit()


    def getUser (self,login):
        sql = f"SELECT * FROM people WHERE login='{login}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]

    def check_login (self):
        sql = "SELECT login FROM people"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        lst = []
        for i in data:
            lst.append(i['login'])
        return lst

    def check_mark (self, login):
        sql = f"SELECT Mатематика, Физика, Биология, Русский, Информатика FROM students WHERE login='{login}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]


    def check_kurs (self,login):
        sql = f"SELECT Курс FROM students WHERE login='{login}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]

    def check_initials (self,login):
        sql = f"SELECT ФИО FROM students WHERE login='{login}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]

    def change_kurs (self):
        sql = "SELECT id, ФИО, Курс FROM students"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data

    def get_id (self,id):
        sql = f"SELECT ФИО, Курс FROM students WHERE id='{id}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]

    def add_Kurs(self,kurs,id):
        sql = f"UPDATE students SET Курс = '{kurs}' WHERE id = '{id}'"
        self.cursors.execute(sql)
        self.connection.commit()

    def check_marks (self,id):
        sql = f"SELECT Mатематика, Физика, Биология, Русский, Информатика FROM students WHERE id ='{id}'"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        return data[0]

    def change_marks(self,id,mathematics,physics,biology,computer_science,russian):
        sql = f"UPDATE students SET `Mатематика` = '{mathematics}',`Физика` = '{physics}'," \
              f"`Биология` = '{biology}',`Информатика` = '{computer_science}'," \
              f"`Русский` = '{russian}' WHERE `id` = '{id}'"
        self.cursors.execute(sql)
        self.connection.commit()
