import sys

def tracker():
    while True:
        print("Current progress: example")
        while True:
            user_input = input("Do you want to update your progress? y/n: ")

            if user_input == "y":
                print("y")
            elif user_input == "n":
                break
        break