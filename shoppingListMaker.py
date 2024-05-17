#The aim of this assignment is to create a program that helps users make a shopping list.

#Task 1: Write a function that lets the user add items to a list.
#Task 2: Include a feature to remove items from the list.
#Task 3: Add a function that prints out the entire list in a formatted way.
shopping_list_items = []
def show_shopping_list():
    global shopping_list_items
    print("\nShopping List:")
    for items in shopping_list_items:
        print(items)           

def shopping_list_assistant():
    global shopping_list_items   
    while True:       
        option = input("Choose an option: [A]dd item / [R]emove item / [S]how list / [Q]uit: ").upper()
        if option == 'A':
            new_item = input("What would you like to add to the list?: ")
            shopping_list_items.append(new_item)
            print(f"{new_item} added to your shopping list.")
        elif option == 'R':
            removed_item = input("Which item would you like to remove?: ")
            shopping_list_items.remove(removed_item)
            print(f"{removed_item} has been taken off of your shopping list.")
        elif option == 'S':
            show_shopping_list()
        elif option == "Q":
            break
        else:
            print("Invalid entry. Please try again.")
shopping_list_assistant()




