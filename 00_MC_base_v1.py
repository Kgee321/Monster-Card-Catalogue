""" Base Component -- Version 1
Welcome screen and message created here
Pre-Monster cards added to a dictionary inside a dictionary here
Adding each component as they are created
Not much editing done to the code
When input code entered, changing it to use
the char_boundary function to put word
limit on inputs.
Added components 1, 2, and 3.
Written by Katelyn Gee
Created on the 1/05/2023
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


# Monster Cards Catalogue stored
monster_cards = {
    "Stoneling":
        {"Strength": 7,
         "Speed": 1,
         "Stealth": 25,
         "Cunning": 15},
    "Vexscream":
        {"Strength": 1,
         "Speed": 6,
         "Stealth": 21,
         "Cunning": 19},
    "Dawnmirage":
        {"Strength": 5,
         "Speed": 15,
         "Stealth": 18,
         "Cunning": 22},
    "Blazegolem":
        {"Strength": 15,
         "Speed": 20,
         "Stealth": 23,
         "Cunning": 6},
    "Websnake":
        {"Strength": 7,
         "Speed": 15,
         "Stealth": 10,
         "Cunning": 5},
    "Moldvine":
        {"Strength": 21,
         "Speed": 18,
         "Stealth": 14,
         "Cunning": 5},
    "Vortexwing":
        {"Strength": 19,
         "Speed": 13,
         "Stealth": 19,
         "Cunning": 2},
    "Rotthing":
        {"Strength": 16,
         "Speed": 7,
         "Stealth": 4,
         "Cunning": 12},
    "Froststep":
        {"Strength": 14,
         "Speed": 14,
         "Stealth": 17,
         "Cunning": 4},
    "Wispghoul":
        {"Strength": 17,
         "Speed": 19,
         "Stealth": 3,
         "Cunning": 2}
}

# Welcome and Instructions
easygui.msgbox("Welcome to Monster Card Catalogue! \n"
               "You have the option to add a Card, "
               "search cards, delete a card, "
               "or show all the cards in this program. "
               "Please select what you would "
               "like to do on the next page."
               "\nEnjoy!", "Welcome and Instructions")

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
