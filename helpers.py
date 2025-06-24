# All helper functions go here
import json

def printer(filename: str):
    with open(f"{filename}", "a") as storage:
        print(storage)


def add_to_json(filename: str, temp_list: list):
    temp_dict = {}
    for idx in temp_list:
        test = {idx: "0"}
        temp_dict.update(test)
        # IN PROGRESS, DOES NOT WORK YET

    with open(f"{filename}", "a") as storage:
        json.dump(temp_dict, storage)