import sys
import helpers
import re

def scheduler():
    while True:
        user_input = input("(1) See current schedule, (2) Create new schedule, (3) Modify current schedule or (4) Set up non negotiable hours: ").lower()

        # See current schedule
        if user_input == "1":
            while True:
                print(helpers.scheduler_read())
                user_input = input("Do you want to upload schedule to Google Calendar? y/n: ").lower()

                # Yes
                if user_input == "y":
                    print("Uploading schedule to Google Calendar...")
                    helpers.insert_to_calendar()
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
                            if helpers.scheduler_read() == "empty":
                                print("There is no previous schedule.")
                                continue
                            print(helpers.scheduler_read())
                            loop_checker = True

                            # call the next while loop function for keep_list
                            helpers.scheduler_keepdata_loop(length_input)

                            if helpers.scheduler_keepdata_loop == "k" or helpers.scheduler_keepdata_loop == "b":
                                break

                        # No
                        elif keepdata_input == "n":
                            # Start generating schedule
                            print("Generating new schedule")
                            helpers.scheduler_write(helpers.scheduler(length_input))
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

            print(helpers.scheduler_read())
            while True:
                user_input = input("Which day would you like to modify?: ").lower()
                loop_checker = False

                # Testing if input is int
                try:
                    int(user_input)

                    while True:
                        print(helpers.scheduler_read(user_input))
                        modify_input = input("Modify your schedule in following format: 00:00-01:00, example , (d) when Done: ").lower()

                        # Back
                        if modify_input == "b":
                            break

                        elif modify_input == "q":
                            sys.exit("Quitting...")

                        elif modify_input == "d":
                            loop_checker = True
                            break

                        elif re.search(r"^([01][0-9]|2[0-3]):([0-5][0-9])-([01][0-9]|2[0-3]):([0-5][0-9]), ", modify_input):
                            helpers.scheduler_modify(modify_input, int(user_input) - 1)

                        else:
                            print("Check your formatting and try again.")
                            
                        
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
                print(helpers.scheduler_noneg_read())
                # Later should create opportunity to select days where you want to apply nonneg hours
                user_input = input("Do you want to (1) Add new hours or (2) Modify current hours: ").lower()

                # Add new hours
                if user_input == "1":
                    noneg_temp = []
                    while True:
                        noneg_input = input("Add non negotiable hours, in following format: 00:00-01:00, example , (d) when Done: ").lower()
                        
                        if noneg_input == "b":
                            noneg_temp = []
                            break

                        elif noneg_input == "d":
                            # Pass the temp list to scheduler_noneg 
                            helpers.scheduler_noneg(noneg_input, noneg_temp)
                            noneg_temp = []
                            break

                        elif noneg_input == "q":
                            sys.exit("Quitting...")

                        elif re.search(r"^([01][0-9]|2[0-3]):([0-5][0-9])-([01][0-9]|2[0-3]):([0-5][0-9]), ", noneg_input):

                            # split string in to 3 parts, start_time, end_time, task
                            time_range, task = noneg_input.split(",", 1)
                            start_time, end_time = time_range.strip().split("-", 1)

                            data_dictionary = {"start": start_time, "end": end_time, "task": task}
                            noneg_temp.append(data_dictionary)
                            print(noneg_temp)

                        else:
                            print("Check your formatting and try again.")
                        
                # Modify current hours
                elif user_input == "2":
                    noneg_temp = []
                    noneg_data = helpers.scheduler_noneg_read()
                    if noneg_data == "No non negotiable hours, add some!":
                        continue
                    else:
                        while True:
                            noneg_input = input("Modify non negotiable hours, in following format: 00:00-01:00, example , (d) when Done: ").lower()                        
                            
                            if noneg_input == "b":
                                noneg_temp = []
                                break

                            elif noneg_input == "d":
                                # Pass the temp list to noneg_write
                                helpers.scheduler_noneg_modify(noneg_temp)
                                noneg_temp = []
                                break

                            elif noneg_input == "q":
                                sys.exit("Quitting...")

                            elif re.search(r"^([01][0-9]|2[0-3]):([0-5][0-9])-([01][0-9]|2[0-3]):([0-5][0-9]), ", noneg_input):

                                # split string in to 3 parts, start_time, end_time, task
                                time_range, task = noneg_input.split(",", 1)
                                start_time, end_time = time_range.strip().split("-", 1)

                                data_dictionary = {"start": start_time, "end": end_time, "task": task}
                                noneg_temp.append(data_dictionary)
                                print(noneg_temp)

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