
from db.dbconnect import db

class dbupdate():
    def update_ticket(todo_list_id, new_title, new_desc, new_due_date, new_priority, new_status):
        try:

            db_connection = db.db_connect()

            sql = """UPDATE todo_list SET title = %s, description = %s, due_date = %s, priority = %s, status = %s WHERE todo_list_id = %s"""

            value = (new_title, new_desc, new_due_date, new_priority, new_status, todo_list_id)

            cursor = db_connection.cursor()
            cursor.execute(sql, value)

            db_connection.commit()

            return True
        except Exception as e:
            print(e)
            return False

    def update_user(userid, username, password, firstname, lastname):
        try:
            db_connection = db.db_connect()
            sql = """UPDATE user SET username = %s, password = %s WHERE user_id = %s"""
            user_value = (username, password, userid)

            cursor = db_connection.cursor()
            cursor.execute(sql, user_value)

            db_connection.commit()

            sql = """UPDATE user_info SET firstname = %s, lastname = %s WHERE user_id = %s"""
            user_info_value = (firstname, lastname, userid)

            cursor = db_connection.cursor()
            cursor.execute(sql, user_info_value)

            db_connection.commit()

            return True

        except Exception as e:
            print(e)
            return False