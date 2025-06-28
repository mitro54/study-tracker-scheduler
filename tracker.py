import sys
import helpers

def tracker():
    while True:
        helpers.printer("tracker.json")

        while True:
            user_input = input("Do you want to add new topics or update your progress? (1) Yes / (2) No: ").lower()

            # Yes
            if user_input == "1":
                while True:
                    helpers.printer("tracker.json")
                    user_input = input("Do you want to (1) Add new topics or (2) Update current progress?: ").lower()

                    # Add new topics
                    if user_input == "1":
                        temp_storage = []
                        while True:
                            user_input = input("Please input a topic, (d) when Done: ")

                            if user_input == "d":
                                helpers.add_to_tracker_json("tracker.json", temp_storage)
                                temp_storage = []
                                break

                            elif user_input == "b":
                                temp_storage = []
                                break

                            temp_storage.append(user_input)

                    
                    # Update current topics
                    elif user_input == "2":
                        while True:
                            helpers.printer("tracker.json")
                            user_input = input("Please select a topic to update: ")
                            if user_input == "" or user_input == "b":
                                break
                            helpers.update_tracker_progress("tracker.json", user_input)
                            
                    elif user_input == "b":
                        break
                    elif user_input == "q":
                        sys.exit("Quitting...")              
            
            # No or Back
            elif user_input == "2" or user_input == "b":
                break
            elif user_input == "q":
                sys.exit("Quitting...")
        break