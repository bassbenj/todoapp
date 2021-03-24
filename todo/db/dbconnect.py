
from mysql.connector import connect, Error

class db():
    def db_connect():
        try:
            db = connect(
                host= "localhost",
                user= "root",
                password= "")

            cursor = db.cursor()
            cursor.execute('create database if not exists todo')

            db = db = connect(
                host= "localhost",
                user= "root",
                password= "",
                database="todo")

            return db

        except Exception as e:
            print(e)

    def db_create():
        try:
            db_connection = db.db_connect()
            cursor = db_connection.cursor()
            sql_file = open("todo.sql")
            sql = sql_file.read()
            cursor.execute(sql, multi=True)

        except Exception as e:
            print(e)

