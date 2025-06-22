import sys

def scheduler():
    while True:
        user_input = input("(1) See current schedule, (2) Create new schedule, (3) Modify current schedule or (4) Set up non negotiable hours: ").lower()

        # See current schedule
        if user_input == "1":
            while True:
                print("Full schedule prints here")
                user_input = input("Do you want to upload schedule to Google Calendar? y/n: ").lower()

                # Yes
                if user_input == "y":
                    print("Uploading schedule to Google Calendar...")
                    # If ok ... print "success!"
                    break
                
                # No or Back
                elif user_input == "n" or user_input == "b":
                    break
                elif user_input == "q":
                    sys.exit("Quitting...")

        # Create new schedule
        elif user_input == "2":
            while True:
                user_input = input("Please provide your new schedule a length in days: ").lower()

                # Testing if input is int
                try:
                    int(user_input)

                    while True:
                        user_input = input("Keep any data from previous schedule? y/n: ").lower()
                        loop_checker = False

                        # Yes
                        if user_input == "y":
                            print("Previous schedule gets printed here")
                            loop_checker = True

                            while True:
                                user_input = input("What to keep? Format: day/hourstart:minute, day/hourend:minute (write k when done): ")

                                # Okay
                                if user_input == "k":
                                    # Then erase everything else from the JSON file and start generating new schedule, will create separate functions for this task
                                    break
                        
                        # No
                        elif user_input == "n":
                            # Start generating schedule, will create separate functions for this task once main frame is done
                            print("Generating new schedule")
                            loop_checker = True
                            break
                        
                        # Back
                        elif user_input == "b":
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
                    
                    # Back
                    if user_input == "b":
                        break

                    elif user_input == "q":
                        sys.exit("Quitting...")

        # Modify current schedule
        elif user_input == "3":

            print("Current schedule gets printed here")
            while True:
                user_input = input("Which day would you like to modify?: ").lower()
                loop_checker = False

                # Testing if input is int
                try:
                    int(user_input)
                    input_holder = {}

                    while True:
                        print("Selected days schedule prints here")
                        user_input = input("Modify your schedule in following format: 00:00-01:00: example , (d) when Done: ").lower()

                        # Back
                        if user_input == "b":
                            input_holder = {}
                            break

                        elif user_input == "q":
                            sys.exit("Quitting...")
                        

                        # If user_input passes regex, prepare it for the dictionary and then push it to dictionary                     
                        # input_holder.update(user_input)
                        
                        # After user is done, push the input_holders data to JSON, clear input_holder
                        if user_input == "d":
                            input_holder = {}
                            loop_checker = True
                            break
                        
                    if loop_checker:
                        break
                        
                # If input is not int, do not raise error
                except ValueError:
                        
                        # Back
                        if user_input == "b":
                            break

                        elif user_input == "q":
                            sys.exit("Quitting...")

        # Set up non negotiable hours 
        elif user_input == "4":
            print("4")

        # Back
        elif user_input == "b":
            break

        elif user_input == "q":
            sys.exit("Quitting...")