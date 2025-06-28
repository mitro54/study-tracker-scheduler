# All helper functions go here
import json

def printer(filename: str):
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
