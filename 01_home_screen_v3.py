""" Component 1 -- Home Screen (version 3)
This code is changing 01_home_screen_v2.
Instead of input statements used, Easygui button box
is used to make code shorter and nicer for the user to use.
A loop is also no longer needed as
there is no way the user can enter the wrong input.
Written by Katelyn Gee
Created on the 30/04/2023
"""

import easygui

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
    print("User wants to leave")





