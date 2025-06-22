import sys

def scheduler():
    while True:
        user_input = input("(1) See current schedule, (2) Create new schedule, (3) Modify current schedule or (4) Set up non negotiable hours: ").lower()

        if user_input == "1": # See current schedule
            while True:
                print("Full schedule prints here")
                user_input = input("Do you want to upload schedule to Google Calendar? y/n: ").lower()

                if user_input == "y": # Yes
                    print("Uploading schedule to Google Calendar...")
                    # If ok ... print "success!"
                    break

                elif user_input == "n" or user_input == "b": # No or Back
                    break
                elif user_input == "q":
                    sys.exit("Quitting...")

        elif user_input == "2": # Create new schedule
            while True:
                user_input = input("Please provide your new schedule a length in days: ").lower()

                # Testing if input is int
                try:
                    int(user_input)

                    while True:
                        user_input = input("Keep any data from previous schedule? y/n: ").lower()
                        loop_checker = False

                        if user_input == "y": # Yes
                            print("Previous schedule gets printed here")
                            loop_checker = True

                            while True:
                                user_input = input("What to keep? Format: day/hourstart:minute, day/hourend:minute (write k when done): ")

                                if user_input == "k": # Okay
                                    # Then erase everything else from the JSON file and start generating new schedule, will create separate functions for this task
                                    break

                        elif user_input == "n": # No
                            # Start generating schedule, will create separate functions for this task once main frame is done
                            print("Generating new schedule")
                            loop_checker = True
                            break

                        elif user_input == "b": # Back
                            break

                        elif user_input == "q":
                            sys.exit("Quitting...")
                        
                        # Break out of the loop if user has visited y or n
                        if loop_checker:
                            break

                    # Break out of outer loop to get back to menu
                    break

                # If input is not int, do not raise error
                except ValueError:

                    if user_input == "b": # Back
                        break

                    elif user_input == "q":
                        sys.exit("Quitting...")


        elif user_input == "3": # Modify current schedule
            print("Current schedule gets printed here")
        elif user_input == "4": # Set up non negotiable hours
            print("4")

        elif user_input == "b": # Back
            break
        
        elif user_input == "q":
            sys.exit("Quitting...")