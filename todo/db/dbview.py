
from db.dbconnect import db

class dbview():
    def view_user(username):
        db_connection = db.db_connect()

        sql = """SELECT * FROM user WHERE username = %s"""

        cursor = db_connection.cursor()
        cursor.execute(sql, (username,))

        result = cursor.fetchone()

        return result

    def view_list_by_user(userid):

        db_connection = db.db_connect()

        sql = """SELECT * FROM todo_list WHERE user_id = %s"""

        cursor = db_connection.cursor()

        cursor.execute(sql, (userid,))
        return cursor.fetchall()

    def view_list_by_id(todo_list_id):
        db_connection = db.db_connect()

        sql = """SELECT * FROM todo_list WHERE todo_list_id = %s"""

        cursor = db_connection.cursor()

        cursor.execute(sql, (todo_list_id,))
        return cursor.fetchone()

    def view_user_info(userid):
        db_connection = db.db_connect()

        sql = """SELECT * FROM user u INNER JOIN user_info ui ON u.user_id = ui.user_id WHERE u.user_id = %s"""

        cursor = db_connection.cursor()

        cursor.execute(sql, (userid,))
        return cursor.fetchone()