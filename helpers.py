# All helper functions go here
import json

def printer(filename: str):
    with open(f"{filename}", "a") as storage:
        print(storage)


def add_to_json(filename: str, temp_list: list):
    dict_list = []
    temp_dict = {}
    with open(f"{filename}", "r+") as storage:
        storage.seek(0,2)
        if storage.tell() == 0:
            for idx in temp_list:
                test = {idx: "0"}
                temp_dict.update(test)
                # IN PROGRESS, DOES NOT WORK YET
            dict_list.append(temp_dict)
            json.dump(dict_list, storage)
        else:
            print("not empty")