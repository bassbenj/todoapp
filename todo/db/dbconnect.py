
from mysql.connector import connect, Error

class db():
    def db_connect():
        try:
            db = connect(
                host= "localhost",
                user= "root",
                password= "",
                database= "todo")

            return db

        except Exception as e:
            print(e)

if __name__ == '__main__':
    pass