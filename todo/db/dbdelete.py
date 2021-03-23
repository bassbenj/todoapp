from db.dbconnect import db

class dbdelete():
    def delete_ticket(todo_list_id):
        try:

            db_connection = db.db_connect()

            sql = """DELETE FROM todo_list WHERE todo_list_id = %s"""

            cursor = db_connection.cursor()
            cursor.execute(sql, (todo_list_id,))

            db_connection.commit()

            return True

        except Exception as e:
            print(e)
            return False

    def delete_user_by_id(userid):
        try:
            db_connection = db.db_connect()

            sql = """DELETE FROM user WHERE user_id = %s"""

            cursor = db_connection.cursor()
            cursor.execute(sql, (userid,))

            db_connection.commit()

            return True

        except Exception as e:
            print(e)
            return False

    def delete_user_by_username(username):
        try:
            db_connection = db.db_connect()

            sql = """DELETE FROM user WHERE username = %s"""

            cursor = db_connection.cursor()
            cursor.execute(sql, (username,))

            db_connection.commit()

            return True

        except Exception as e:
            print(e)
            return False