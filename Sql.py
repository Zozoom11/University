
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

    def checklogin (self):
        sql = "SELECT login FROM `people`"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        lst = []
        for i in data:
            lst.append(i['login'])
        return lst

