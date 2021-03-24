
from view.main import main
from db.dbconnect import db


if __name__ == '__main__':
    print("Welcome to the to do list app.")
    try:
        db.db_connect()
        db.db_create()
    except Exception as e:
        print('database ready')
    main.main()