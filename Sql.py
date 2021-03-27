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
        sql = "INSERT INTO people (name,login,password,status) VALUES (%s, %s, %s, %s)"
        temp = [name,login,password,status]
        self.cursors.execute(sql,temp)
        self.connection.commit()

    def getUsers(self):
        sql = "SELECT * FROM users"
        self.cursors.execute(sql)
        data = self.cursors.fetchall()
        print(data)
