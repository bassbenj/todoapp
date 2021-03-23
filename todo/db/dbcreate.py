
from datetime import datetime

from db.dbconnect import db
from db.dbview import dbview

class dbcreate():
    def create_user(user, password, firstname, lastname):
        try:
            db_connection = db.db_connect()
            
            
            sql = """INSERT INTO user (username, password) VALUES (%s, %s)"""
            user_record = (user, password)

            cursor = db_connection.cursor()
            cursor.execute(sql, user_record)

            db_connection.commit()
            
            sql = """INSERT INTO user_info (user_id, firstname, lastname) VALUES (%s, %s, %s)"""
            
            user_value = dbview.view_user(user)
            user_info_record = (user_value[0], firstname, lastname)

            cursor = db_connection.cursor()
            cursor.execute(sql, user_info_record)

            db_connection.commit()

            return True
        
        except Exception as e:
            return False


    def create_ticket(userid, title, desc, duedate, priority, status):
        try:
            print("creating ticket")
            db_connection = db.db_connect()

            sql = """INSERT INTO todo_list (user_id, title, description, due_date, priority, status) VALUES (%s, %s, %s, %s, %s, %s)"""

            todo_value = (userid, title, desc, duedate, priority, status.capitalize())

            cursor = db_connection.cursor()
            cursor.execute(sql, todo_value)

            db_connection.commit()

            return True

        except Exception as e:
            print(e)
            return False
