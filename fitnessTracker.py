#Objective:
#The aim of this assignment is to create a program that tracks fitness activities and calories burned.

#Task 1: Develop a function to log different fitness activities and their duration. For instance, activities = [’Dancing’, ‘Swimming’, 
#‘Biking’] and duration = [10, 20, 15] where Dancing corresponds to 10 minutes, Swimming corresponds to 20 minutes, and Biking 
#corresponds to 15 minutes.

#Task 2: Write a simple function that estimates calories burned based on the activity and duration. For instance, Total calories 
#burned = Duration (in minutes)*3.5

#Task 3: Create a summary function that provides a report of all activities and total calories burned for the day.

activity = []
duration = []
def fitness_tracker():
    global activity
    global duration    
    new_activity = input("What activity did you perform?: ")
    activity.append(new_activity)
    activity_duration = int(input("How many minutes did you spend on that activity?: "))
    duration.append(activity_duration)
    print(f"{new_activity} has been added for a length of {activity_duration} minutes.")
def fitness_report():
    global activity
    global duration
    calories_burned = sum(duration) * 3.5
    print(f"The activities you've performed today are: {activity}")
    print(f"You have burned {calories_burned} calories today!")
while True:
    action = input("Choose an action: [I]nput Activity, [V]iew Fitness Report, [Q]uit Program: ").upper()
    if action == 'I':
        fitness_tracker()
    elif action == 'V':
        fitness_report()
    elif action == 'Q':
        break
    else:
        print("Invalid entry, please try again.")



    