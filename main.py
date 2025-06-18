import scheduler
import tracker

def main():
    while True:
        user_input = input("Welcome to Study Tracker/Scheduler. Please select (1) Schedule or (2) Tracking to continue: ")

        if user_input == "1":
            scheduler.scheduler()
        elif user_input == "2":
            tracker.tracker()
        elif user_input == "q":
            break
        
if __name__ == '__main__':
    main()