
import os
import importlib
import getpass

from view.todolist import todolist

class main():
    def main():
        #Number of errors
        i = 3
        counter = 0

        while counter <= i:

            print("Please select from the folowing:")
            print("1. Login")
            print("2. Create User")
            print("3. Delete User")
            print("4. Exit")
            try:
                selection = int(input("Please Select: "))

                os.system('cls' if os.name == 'nt' else 'clear')
                
                if selection == 1:
                    main.login_user()
                    break
                elif selection == 2:
                    main.create_user()
                    break
                elif selection == 3:
                    main.delete_user()
                    break

                elif selection == 4:
                    print("Thank you for using my to do app. Bye!")
                    break
                else:
                    print("Wrong selection.")
            except Exception as e:
                print("Wrong selection.")

            counter += 1


    def login_user():
        i = 0
        while i < 3:
            print("Login")
            userlogin = input("Username: ")
            password = getpass.getpass(prompt = "Password: ")

            if userlogin:
                db = importlib.import_module('db.dbview').dbview.view_user(userlogin)
                if db[2] != password:
                    print("wrong password.")
                else:
                    todolist.view_list(db[0])
                    break
            else:
                print("Username does not exist.")

            i += 1

        os.system('cls' if os.name == 'nt' else 'clear')
        main.main()


    def create_user():
        proceed = input("Proceed in creating user?[Y/N]")
        if proceed in ['Y', 'y']:
            
            print("Create new User.")
            firstname = input("First name: ")
            lastname = input("Last name: ")

            i = 1
            while i < 10:    
                userlogin = input("Username: ")
                password = getpass.getpass(prompt = "Password: ")

                db = importlib.import_module('db.dbcreate').dbcreate.create_user(userlogin, password, firstname, lastname)

                if db == False:
                    print("User already exist.")
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("You have created a new user.")
                    main.main()

                main.main()
                i += 1

        elif proceed in ['N', 'n']:
            os.system('cls' if os.name == 'nt' else 'clear')
            main.main()

    def delete_user():
        proceed = input("Proceed in Deleting user?[Y/N]")

        if proceed in ['Y', 'y']:
            print("Delete user by[Press Enter to go back to main manu]:")
            choice = int(input("[1 to delete by user id or 2 to delete by username]: "))

            if choice == 1:

                del_by_userid = input("Please enter user id: ")
                db_del = importlib.import_module('db.dbdelete').dbdelete.delete_user_by_id(del_by_userid)

                if db_del == True:
                    print("User deleted.")
                    main.main()

            elif choice == 2:

                del_by_username = input("Please enter username: ")
                db_del = importlib.import_module('db.dbdelete').dbdelete.delete_user_by_username(del_by_username)

                if db_del == True:
                    print("User deleted.")
                    main.main()
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                main.main()


        elif proceed in ['N', 'n']:
            os.system('cls' if os.name == 'nt' else 'clear')
            main.main()
