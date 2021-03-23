

import importlib
import os
import getpass

from datetime import datetime
from prettytable import PrettyTable

class todolist():
    def view_list(userid):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        db = importlib.import_module('db.dbview').dbview.view_list_by_user(userid)
        db_user = importlib.import_module('db.dbview').dbview.view_user_info(userid)

        if db:
            print("Hi, ", db_user[6])
            print("Here are your to-do list.")
            table = PrettyTable(['Title', 'Description', 'Due Date', 'Priority', 'Status'])
            table.align = 'l'
            for row in db:
                table.add_row([row[2], row[3], row[4].strftime('%m %d %Y'), row[5], row[6]])
            print(table)
        else:
            print("Nothing to do today!")

        print("What do you want to do today?")
        print("1. Add something on the list")
        print("2. Edit list")

        print("3. Delete list")
        print("4. Edit user")
        print("5. Logout")
        selection = int(input("Select: "))
        print(selection)

        if selection == 1:
            todolist.create_todo(userid)
        elif selection == 2:
            todolist.edit_todo(userid)
        elif selection == 3:
            todolist.delete_todo(userid)
        elif selection == 4:
            todolist.edit_user(userid)
        elif selection == 5:
            os.system('cls' if os.name == 'nt' else 'clear')
            from view.main import main
            main.main()


    def create_todo(userid):
        
        title = input("Title: ")
        desc = input("Description: ")
        print("Press enter if the due date is today.")
        
        duedate = input("Due date [MM-DD-YYYY]: ")
        if duedate in [None, '', 0]:
            now = datetime.now()
            duedate = now.strftime('%Y-%m-%d')
        else:
            duedate = datetime.strptime(duedate, '%m-%d-%Y')
        
        priority = input("Priority [1-5]: ")
        if priority == '':
            priority = 3

        status = 'New'
        if status is None:
            status = 'New'

        db = importlib.import_module('db.dbcreate').dbcreate.create_ticket(userid, title, desc, duedate, priority, status)

        todolist.view_list(userid)


    def edit_todo(userid):
        os.system('cls' if os.name == 'nt' else 'clear')
        db = importlib.import_module('db.dbview').dbview.view_list_by_user(userid)

        table = PrettyTable(['Id', 'Title', 'Description', 'Due Date', 'Priority', 'Status'])
        table.align = 'l'
        for row in db:
            table.add_row([row[0], row[2], row[3], row[4].strftime('%m %d %Y'), row[5], row[6]])

        print(table)
        i = 0
        while i <= 3:
            todo_list_id = int(input("Which to do list do you want to update? [Enter ID]: "))

            for row in db:
                if todo_list_id == row[0]:
                    db_by_todolist = importlib.import_module('db.dbview').dbview.view_list_by_id(todo_list_id)
                    try:
                        new_title = input("Title[%s]: " % row[2])
                        if new_title == '':
                            new_title = row[2]

                        new_desc = input("Description[%s]: " % row[3])
                        if new_desc == '':
                            new_desc = row[3]

                        new_due_date = input("Due Date[%s]: " % row[4].strftime('%m %d %Y'))
                        if new_due_date == '':
                            new_due_date = row[4]

                        new_priority = input("Priority[1-5][%s]: " % str(row[5]))
                        if new_priority == '':
                            new_priority = row[5]

                        new_status = input("Status[New/On Going/Done][%s]: " % row[6])
                        if new_status == '':
                            new_status = row[6]


                        db_by_todolist = importlib.import_module('db.dbupdate').dbupdate.update_ticket(todo_list_id, new_title, new_desc, new_due_date, new_priority, new_status)
                    except Exception as e:
                        todolist.view_list(userid)


            if db_by_todolist == True:
                todolist.view_list(userid)
                break

            print("Not in the list")
            i += 1

    def delete_todo(userid):
        os.system('cls' if os.name == 'nt' else 'clear')
        db = importlib.import_module('db.dbview').dbview.view_list_by_user(userid)

        table = PrettyTable(['ID', 'Title', 'Description', 'Due Date', 'Priority', 'Status'])
        table.align = 'l'
        for row in db:
            table.add_row([row[0], row[2], row[3], row[4].strftime('%m %d %Y'), row[5], row[6]])

        print(table)
        print("Press enter to go back to main menu.")
        todo_list_id = input("Select task to delete [Enter ID]: ")

        if todo_list_id == '':
            todolist.view_list(userid)
        else:
            db_list_delete = importlib.import_module('db.dbdelete').dbdelete.delete_ticket(todo_list_id)
            print(db_list_delete)
            if db_list_delete == True:
                todolist.view_list(userid)


    def edit_user(userid):
        
        db = importlib.import_module('db.dbview').dbview.view_user_info(userid)

        table = PrettyTable(['Username', 'First name', 'Lastname'])
        table.align = 'l'

        table.add_row([db[1], db[6], db[7]])

        print(table)

        proceed = input("do you want to edit info?[Y/N]")

        if proceed.lower() == 'y':
            firstname = input("First name: ")
            if firstname == '':
                firstname = db[6]

            lastname = input("Last name: ")
            if lastname == '':
                lastname = db[7]

            userlogin = input("Username: ")
            if userlogin == '':
                userlogin = db[1]
            
            password = getpass.getpass(prompt = "Password: ")
            if password == '':
                password = db[2]

            db_user_update = importlib.import_module('db.dbupdate').dbupdate.update_user(userid, userlogin, password, firstname, lastname)
            if db_user_update == True:
                todolist.view_list(userid)


        elif proceed.lower() == 'n':
            todolist.view_list(userid)


