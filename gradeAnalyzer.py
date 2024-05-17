#Objective:
#The aim of this assignment is to analyze a set of grades and provide statistics.

#Task 1: Code a function to calculate the average grade.
#Task 2: Implement a function to find the highest and lowest grade.
#Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).

grades = [80, 95, 73, 84, 78, 92, 99, 71]

def calculate_average_grade():
    global grades
    average = sum(grades) / len(grades)
    return average

def highest_lowest():
    global grades
    highest_grade = max(grades)
    lowest_grade = min(grades)
    print(f"The lowest grade is {lowest_grade}")
    print(f"The highest grade is {highest_grade}")

def letter_grade():
    global grades
    for grade in grades:
        if grade < 70:
            grade = 'F'
        elif grade >= 70 and grade <= 75:
            grade = 'D'
        elif grade >= 76 and grade <= 80:
            grade = 'C'
        elif grade >= 81 and grade <= 85:
            grade = 'B'
        elif grade >= 86 and grade <= 90:
            grade = 'A'
        else:
            grade = 'A+'
        print(grade)

while True:
    print("\nWhat would you like to display?")
    print("1. Average Grade")
    print("2. Highest and Lowest Grades")
    print("3. Grades Converted to Letter Grade")
    print("4. Exit Program")
    action = input("Enter your choice: ")
    if action == '1':
        average_grade = calculate_average_grade()
        print(f"The average of all grades is: {average_grade}")

    elif action == '2':
        highest_lowest()

    elif action == '3':
        letter_grade()
    elif action == '4':
        break
    else:
        print("Invalid entry. Please try again.")



