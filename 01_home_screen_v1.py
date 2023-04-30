""" Component 1 -- Home Screen (version 1)
This code is the beginning of creating Monster Cards home screen.
This code will not use easygui to begin with
and print statements will be used and deleted
later to test if code is working.
Written by Katelyn Gee
Created on 30/04/2023
"""

# Asking user what they want to do with the monster cards
options = input("Enter what you would like to do with the Monster Cards: \n"
                "Enter Add to add a cards \n"
                "Enter Search to search all cards \n"
                "Enter Delete to delete a card \n"
                "Enter Print to print all cards \n"
                "Enter Exit to leave \n")

# If user want to a card
if options == "add":
    print("User wants to add a card")

# If user wants to search for cards
elif options == "search":
    print("User wants to search cards")

# If user wants to delete a card
elif options == "delete":
    print("User wants to delete a card")

# If user want to print all cards
elif options == "print":
    print("User wants all cards printed")

# If user want to leave code
elif options == "exit":
    print("User wants to leave")

# If an incorrect code entered
else:
    print("Wrong input entered")



