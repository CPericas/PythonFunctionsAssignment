#Objective:
#The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.

#Task 1: Create functions for each arithmetic operation.
#Task 2: Implement user input to receive numbers and an operation choice.
#Task 3: Ensure your program can handle division by zero and other potential errors.

def addition(num1, num2):
    global addition
    result = num1 + num2
    return result

def subtraction (num1, num2):
    global subtraction
    result = num1 - num2
    return result

def multiplication(num1, num2):
    global multiplication
    result = num1 * num2
    return result

def division(num1, num2):
    global division
    if num1 or num2 == 0:
        result = 0
    else:
        result = num1 // num2 
    return result

while True:
    action = input("Choose an action: [A]ddition / [S]ubtraction / [M]ultiplication / [D]ivision / [Q]uit: ").upper()
    if action == 'A':
        num1 = int(input("Input 1st number: "))
        num2 = int(input("Input 2nd number: "))
        result = addition(num1, num2)
        print(f"{num1} plus {num2} equals: {result}")

    elif action == 'S':
        num1 = int(input("Input 1st number: "))
        num2 = int(input("Input number to subtract from 1st number: "))
        result = subtraction(num1, num2)
        print(f"{num1} minus {num2} equals: {result}")

    elif action == 'M':
        num1 = int(input("Input 1st number: "))
        num2 = int(input("Input 2nd number: "))
        result = multiplication(num1, num2)
        print(f"{num1} times {num2} equals: {result}")

    elif action == 'D':
        num1 = int(input("Input 1st number: "))
        num2 = int(input("Input number to divide 1st number by: "))
        result = division(num1, num2)
        print(f"{num1} divided by {num2} equals: {result}")

    elif action == 'Q':
        break

    else:
        print("Invalid entry, please try again.")


        
