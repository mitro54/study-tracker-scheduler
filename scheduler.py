import sys

def scheduler():
    while True:
        user_input = input("(1) See current schedule, (2) Create new schedule, (3) Modify current schedule or (4) Set up non negotiable hours: ").lower()

        if user_input == "1":
            while True:
                print("Full schedule prints here")
                user_input = input("Do you want to upload schedule to Google Calendar? y/n: ").lower()

                if user_input == "y":
                    print("Uploading schedule to Google Calendar...")
                    # If ok ... print "success!""

                elif user_input == "n" or user_input == "b":
                    break
                elif user_input == "q":
                    sys.exit("Quitting...")

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