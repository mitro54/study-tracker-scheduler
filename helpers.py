# All helper functions go here
import json
import sys
import re

def generate_empty_day():
    # generate a dictionary with 48 keys with empty values
    return {
        f"{h:02d}:{m:02d}": ""
        for h in range(24)
        for m in (0, 30)
    }

def tracking_printer(filename: str):
    with open(f"{filename}", "a+") as storage:

        storage.seek(0,2)
        if storage.tell() == 0:
            print("Tracking has no data yet, add something!")

        else:
            storage.seek(0)
            data = json.load(storage)
            for obj in data:
                for key, value in obj.items():
                    print(f"{key}: {value}")

def add_to_tracker_json(filename: str, temp_list: list):
    dict_list = []
    with open(f"{filename}", "r+") as storage:
        storage.seek(0,2)

        # If file is empty        
        if storage.tell() == 0:
            for idx in temp_list:
                dict_list.append({idx: "0"})

            json.dump(dict_list, storage)
        
        # If file is not empty
        else:
            storage.seek(0)
            existing_data = json.load(storage)

            for idx in temp_list:
                existing_data.append({idx: "0"})

            storage.seek(0)
            storage.truncate()
            json.dump(existing_data, storage)

def update_tracker_progress(filename: str, user_input: str):
    with open(f"{filename}", "r+") as storage:
        storage.seek(0,2)
        
         # If file is empty        
        if storage.tell() == 0:
            print("There is nothing to update. Add new topics first.")
        
        # If file is not empty
        else:
            storage.seek(0)
            existing_data = json.load(storage)

            # Test if user_input matches any key in the list of dictionaries
            if any(obj.get(user_input) for obj in existing_data):

                found_user_input = input(f"Selected {user_input}, update it: ")

                if found_user_input == "b" or found_user_input == "":
                    return
                
                elif found_user_input == "q":
                    print("Quitting...")
                    sys.exit()

                # Find the match, update values
                for obj in existing_data:
                    if user_input in obj:
                        obj.update({user_input: found_user_input})
                
                storage.seek(0)
                storage.truncate()     
                json.dump(existing_data, storage)

            else:
                print(f"Could not find a key: {user_input}")

def scheduler(filename: str, length_input: int, keepdata_input: str, keep_list: list | None = None):
    # Create a temp list that will store each day, each day is a separate dictionary that has pre generated 48 empty slots for the full day, it should print each 30 min slot on a new line, 00:00 - 23:30
    # Note for later, can add another list here if user wants to add something to all days instead of just one.
    temp_list = []

    for i in range(0, int(length_input)):
        # a function call here to generate the dictionary
        day = generate_empty_day()

        # then start filling the day
        while True:
            print("(k) Okay to move to next day, (d) Done to save the current schedule to JSON file. Input format example: 00:00-00:30, reading a book")
            print(f"Currently on day: {i + 1}")
            user_input = input(f"Expecting user input: ")

            # Check if input matches format "starthour:minute-endhour:minute, task
            if re.search(r"^([01][0-9]|2[0-3]):([0-5][0-9])-([01][0-9]|2[0-3]):([0-5][0-9]), ", user_input):

                # split string in to 3 parts, start_time, end_time, task
                time_range, task = user_input.split(",", 1)
                start_time, end_time = time_range.strip().split("-", 1)

                # create new dictionary with times from start_time to end_time, add task to them
                in_range = {
                    time: task
                    for time, task in day.items()
                    if start_time <= time <= end_time
                }

                # iterate over in_range, update key value pairs to match it in day dictionary
                for key in in_range:
                    day[key] = task
                
                # print current full schedule
                for key in day:
                    print(f"{key}:{day.get(key)}")

            elif user_input == "d":
                print(temp_list)
                return temp_list
    
            elif user_input == "k":
            # then append the day to temp_list, move on to next day
                temp_list.append(day)
                break
            
            elif user_input == 'b':
                break

            elif user_input == 'q':
                sys.exit()

            else:
                print("Check your formatting and try again.")

def scheduler_write(temp_list):
    with open(f"scheduler.json", "r+") as storage:
        storage.seek(0,2)

        # If file is empty        
        if storage.tell() == 0:

            json.dump(temp_list, storage)
        
        # If file is not empty
        else:
            storage.seek(0)
            existing_data = json.load(storage)
        
            # Implement logic to save data that is wanted to be kept

            storage.seek(0)
            storage.truncate()
            json.dump(temp_list, storage)

