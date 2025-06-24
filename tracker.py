import sys
import helpers

def tracker():
    while True:
        helpers.printer("tracker.json")
        while True:
            user_input = input("Do you want to add new topics or update your progress? y/n: ").lower()

            # Yes
            if user_input == "y":
                while True:
                    helpers.printer("tracker.json")
                    user_input = input("Do you want to (1) Add new topics or (2) Update current progress?: ").lower()

                    # Add new topics
                    if user_input == "1":
                        while True:
                            user_input = input("Please input a topic, (d) when Done: ")

                            if user_input == "d" or user_input == "b":
                                break
                    
                    # Update current topics
                    elif user_input == "2":
                        while True:
                            print("Topics goes here")
                            user_input = input("Please select a topic to update: ")
                            if user_input == "" or user_input == "b":
                                break
                            # if found, keep going
                            found_user_input = input(f"Selected {user_input}, update it: ")
                            
                    elif user_input == "b":
                        break
                    elif user_input == "q":
                        sys.exit("Quitting...")              
            
            # No or Back
            elif user_input == "n" or user_input == "b":
                break
            elif user_input == "q":
                sys.exit("Quitting...")
        break