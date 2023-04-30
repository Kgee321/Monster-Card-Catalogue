""" Component 1 -- Home Screen version 5 (Final version)
This code is removing the print statements and
replacing them with functions calls.
The functions that are being called on have also
been added although, they have nothing
in them yet (or just pass).
Also testing loop has stayed in the code
so code only ends when user wants it to.
Final code for home_screen.
This code will be in the base component.
Written by Katelyn Gee
Created on 1/05/2023
"""

import easygui


# Adding a new card function
def add():
    pass


# Searching the cards functions
def search():
    pass


# Delete a card functions
def delete():
    pass


# Printing all the cards function
def printing():
    pass


# Loop so code ends when user wants it to
while True:

    # Asking user what they want to do with the monster cards
    options = easygui.buttonbox("Enter what you would like to do with the Monster Cards: \n",
                                "Home Screen",
                                choices=["Add", "Search", "Delete", "Print", "Exit"])

    # If user want to add a card
    if options == "Add":
        add()

    # If user wants to find cards
    elif options == "Search":
        search()

    # If user wants to delete a card
    elif options == "Delete":
        delete()

    # If user want to print all cards
    elif options == "Print":
        printing()

    # If user want to leave code
    elif options == "Exit":

        # Goodbye message outputted and code ends
        easygui.msgbox("Goodbye! Thanks for using Monster Cards", "Leaving Screen")
        break
