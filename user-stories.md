# Study Tracker/Scheduler

## Points of views:
### User:
- AS an user i want to be able to mark down the weeks/periods school topics and own topics
- AS an user i want to be able to hardcode my non negotiable hours for each day (gym, meals, hobbies, freetime, sleep)
- AS an user i want to be able to keep track of progress in certain category
- AS an user i want to keep selected old topics when inserting new topics
- AS an user i want to overwrite last topics by inserting new topics
- AS an user i dont think GUI is necessary
- AS an user i want to be able to generate simple user provided statistics on current progress in all topics
- AS an user i want to be able to push the planned schedule to Google Calendar
- AS an user i want the program	to remember previous data
- AS an user i want the program to be straightforward to use
- AS an user i want the program to be able to go backwards in prompting if needed
- AS an user i want the program to save to a json file instead of a database


#### OPTIONAL (IF you have spare time AND really feel like this is necessary after everything functions)
- AS an user i want to be questioned about the topic on hand by an AI
- AS an user i want to keep studying about the topic on hand until i can answer all AI questions correctly

### Developer:
- AS a developer i want to keep this project as simple as possible
- AS a developer i believe to accomplish this project without the need of AI for any coding
- AS a developer i want this project to be available on github so anyone crazy enough can try it out
- AS a developer i dont think GUI is absolutely necessary
- AS a developer i think this project does not need a database, can use JSON files



## WORKFLOW

**NOTE: At any point user should be able to write (b) to go Back or (q) to Quit without making changes if action is left unfinished**
```
*Program loads all necessary data on startup and then prompts user*

    *user is presented with a choice to select between (1) Schedule and (2) Tracking*
    -> user selects scheduling

        *user is presented with a choice to (1) See current schedule, (2) Create new schedule, (3) Modify current schedule and (4) Set up non negotiable hours*

        -> user selects 1 (See current schedule)
            *Program generates current full schedule and prompts if user wants to upload schedule to Google Calendar y/n*
                -> y
                    *program uploads schedule to Google Calendar, go back to very first prompt*
                -> n
                    *program goes back to previous choice prompt*

        -> user selects 2 (Create new schedule)
            *Program asks user to provide the schedule a duration in number of days*
                -> user input
                    *Program presents a choice to keep any data from previous schedule y/n*
                        -> y
                            *Program generates the previous schedule if there is one and then asks which data to keep, expecting numerical input in format day/hourstart, day/hourend , reprompts until user writes (k) Okay*
                        -> n
                            *Program then starts generating a new schedule based on user input, starting from day 1. It presents full days two slots per hour as example "12.00 - 13.30: Open" or longer slots as "23.00 - 06.00: Sleep (Non negotiable)"*
                            *Input is expected as "starthour.minute-endhour.minute: thing", once user is done with a day, user writes (k) Okay to repeat this process for each day until all days have been scheduled, or user writes (d) Done.*
                            *Program also prints each time the newly updated schedule when user makes an addition to it*

        -> user selects 3 (Modify current schedule)
            *Program prints current schedule and then prompts which day to modify*
                -> user input
                    *Program prompts user that days schedule and expects modifications in format "starthour.minute-endhour.minute: thing", reprompts until user writes (d) Done*
        
        -> user selects 4 (Set up non negotiable hours)
            *Program prints current non negotiable hours (if there are any) and asks user if they want to (1) Add new hours or (2) Modify current hours (If any exist)*
                -> user selects 1 (Add new hours)
                    *input is expected as "starthour.minute-endhour.minute: thing", program goes back to previous prompt after*
                -> user selects 2 (Modify current hours, if any exist)
                    *Program asks user which hours to modify, input is expected as "starthour.minute-endhour.minute: thing", program goes back to previous prompt after*


    -> user selects tracking
        *program generates current tracking information for each topic, then prompts if user wants to update information y/n*
        -> y
            *program then prompts user if they want to (1) Add new topics or (2) Update current topics*
                -> user selects 1 (Add new topics)
                    *program then expects user to input a new topic, saves it to json file, prompts again until user writes (d) Done*
                -> user selects 2 (Update current topics)
                    *program asks which topic to update*
                        -> user input
                            *program then modifies the topic and goes back to previous prompt*
        -> n
            *Program then goes back to the first prompt*
```