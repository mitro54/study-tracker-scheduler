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
                    # If ok ... print "success!"
                    break

                elif user_input == "n" or user_input == "b":
                    break
                elif user_input == "q":
                    sys.exit("Quitting...")

        elif user_input == "2":
            while True:
                user_input = input("Please provide your new schedule a length in days: ").lower()

                # Testing if input is int
                try:
                    int(user_input)

                    while True:
                        user_input = input("Keep any data from previous schedule? y/n: ").lower()

                        if user_input == "y":
                            print("Previous schedule gets printed here")

                            while True:
                                user_input = input("What to keep? Format: day/hourstart:minute, day/hourend:minute (write k when done): ")

                                if user_input == "k":
                                    # Then erase everything else from the JSON file and start generating new schedule, will create separate functions for this task
                                    break

                        elif user_input == "n":
                            # Start generating schedule, will create separate functions for this task once main frame is done
                            print("Generating new schedule")
                            break

                        break
                    break

                # If input is not int, do not raise error
                except ValueError:
                    if user_input == "b":
                        break
                    elif user_input == "q":
                        sys.exit("Quitting...")


        elif user_input == "3":
            print("3")
        elif user_input == "4":
            print("4")
        elif user_input == "b":
            break
        elif user_input == "q":
            sys.exit("Quitting...")