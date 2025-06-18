import sys

def scheduler():
    while True:
        user_input = input("(1) See current schedule, (2) Create new schedule, (3) Modify current schedule and (4) Set up non negotiable hours: ")

        if user_input == "1":
            print("1")
        elif user_input == "2":
            print("2")
        elif user_input == "3":
            print("3")
        elif user_input == "4":
            print("4")
        elif user_input == "b":
            break
        elif user_input == "q":
            sys.exit("Quitting...")