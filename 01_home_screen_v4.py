""" Component 1 -- Home screen (version 4)
This code is the same as 01_home_screen_v3 but a loop is around the code for testing.
Written by Katelyn Gee
Create on 30/04/2023
"""

import easygui

# Loop for testing
while True:

    # Asking user what they want to do with the monster cards
    options = easygui.buttonbox("Enter what you would like to do with the Monster Cards: \n",
                                "Home Screen", choices=["Add", "Search", "Delete", "Print", "Exit"])

    # If user want to add a card
    if options == "Add":
        print("User wants to add a card")

    # If user wants to search for cards
    elif options == "Search":
        print("User wants to search all cards")

    # If user wants to delete a card
    elif options == "Delete":
        print("User wants to delete a card")

    # If user want to print all cards
    elif options == "Print":
        print("User wants all cards printed ")

    # If user want to leave code
    elif options == "Exit":

        # Goodbye message outputted
        easygui.msgbox("Goodbye!", "Leaving Screen")
        print("Program ends")
        break




