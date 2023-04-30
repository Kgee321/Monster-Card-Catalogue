""" Component 1 -- Home Screen (version 2)
This code is adding onto 01_home_screen_v1.
It will put the code in a loop for when wrong
input entered as well as add .lower() so the
capital answers to do not matter
Written by Katelyn Gee
Created on the 30/04/2023
"""

# Loop repeats when wrong input entered
while True:

    # Asking user what they want to do with the monster cards
    options = input("Enter what you would like to do with the Monster Cards: \n"
                    "Enter Add to add a card \n"
                    "Enter Search to search all the cards \n"
                    "Enter Delete to delete a card \n"
                    "Enter Print to print a card \n"
                    "Enter Exit to leave \n").lower()

    # If user want to add a card
    if options == "add":
        print("User wants to add a card")

    # If user wants to search for cards
    elif options == "search":
        print("User wants to search all cards")

    # If user wants to delete a card
    elif options == "delete":
        print("User wants to delete a card")

    # If user want to print combos
    elif options == "print":
        print("User wants all cards printed")

    # If user want to leave code
    elif options == "exit":
        print("User wants to leave")

    # If an incorrect code entered
    else:
        print("Wrong input entered \n ")
        continue

    # Code ends if user input was not a wrong input
    break



