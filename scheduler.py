import sys
import helpers
import re

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
                length_input = input("Please provide your new schedule a length in days: ").lower()

                # Testing if input is int
                try:
                    int(length_input)

                    while True:
                        keepdata_input = input("Keep any data from previous schedule? y/n: ").lower()
                        loop_checker = False
 
                        # Yes
                        if keepdata_input == "y":
                            print("Previous schedule gets printed here")
                            loop_checker = True

                            # call the next while loop function for keep_list
                            while True:
                                helpers.schedule_loop(length_input, keepdata_input)

                                # Okay
                                if helpers.schedule_loop == "k" or helpers.schedule_loop == "b":
                                    break

                        # No
                        elif keepdata_input == "n":
                            # Start generating schedule
                            print("Generating new schedule")
                            helpers.scheduler_write(helpers.scheduler(length_input, keepdata_input))
                            loop_checker = True
                            break
                        
                        # Back
                        elif keepdata_input == "b":
                            break

                        elif keepdata_input == "q":
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
            while True:
                print("Prints non negotiable hours if any exist here")
                user_input = input("Do you want to (1) Add new hours or (2) Modify current hours: ").lower()

                # Add new hours
                if user_input == "1":
                    while True:
                        user_input = input("Add non negotiable hours, in following format: 00:00-01:00: example , (d) when Done: ").lower()

                        # If user_input passes regex, prepare it for the dictionary and then push it to dictionary                     
                        # input_holder.update(user_input)
                        
                        # After user is done, push the input_holders data to JSON, clear input_holder

                        if user_input == "b" or user_input == "d":
                            input_holder = {}
                            break

                        elif user_input == "q":
                            sys.exit("Quitting...")
                        
                # Modify current hours
                elif user_input == "2":
                    while True:
                        user_input = input("Modify non negotiable hours, in following format: 00:00-01:00: example , (d) when Done: ").lower()

                        # If user_input passes regex, prepare it for the dictionary and then push it to dictionary                     
                        # input_holder.update(user_input)
                        
                        # After user is done, push the input_holders data to JSON, clear input_holder
                        
                        if user_input == "b" or user_input == "d":
                            input_holder = {}
                            break

                        elif user_input == "q":
                            sys.exit("Quitting...")

                # Back
                if user_input == "b":
                    break

                elif user_input == "q":
                    sys.exit("Quitting...")

        # Back
        elif user_input == "b":
            break

        elif user_input == "q":
            sys.exit("Quitting...")