# All helper functions go here
import json
import sys

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

def scheduler(filename: str, length_input: str, keepdata_input: str, keep_list: list):
    tuple_list = []   
    with open(f"{filename}", "r+") as storage:
        storage.seek(0,2)

        # If file is empty        
        if storage.tell() == 0:
            for idx in keep_list:
                # Testing if appends, keep_list should not append to json file
                tuple_list.append((idx[0], idx[1]))

            json.dump(tuple_list, storage)
        
        # If file is not empty
        else:
            storage.seek(0)
            existing_data = json.load(storage)
        
            # everything still in progress
            for idx in keep_list:
                # Testing if appends, keep_list should not append to json file
                tuple_list.append((idx[0], idx[1]))

            storage.seek(0)
            storage.truncate()
            json.dump(tuple_list, storage)

