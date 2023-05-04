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


# Function for joinning dictionary's
def joinning(dic):
    message = ""

    # Joinning the dictionary inputted
    for key, value in dic.items():
        message = f"{key}:\n"

        # Formatting dictionary inside dictionary
        for key2, value2 in value.items():
            message += f"- {key2}: {value2} \n"

    return message


# Function for checking characters stay in letter boundary
def char_boundary(lower, upper, question_message, box):
    # Loop for character checker
    while True:
        # Asking user to enter monster card name
        question = easygui.enterbox(question_message, box).title()

        # Upper string boundary
        if len(question) > upper:
            easygui.msgbox("Wrong Input. Please enter less than 20 letters",
                           "Number to high")

        # Lower string boundary
        elif len(question) < lower:
            easygui.msgbox("Wrong Input. Please more than 1 letters",
                           "Number to low")

        # Input correct
        else:
            return question


# Function for adding a new Monster Card
def add():

    # Variable setting
    attributes = ["Strength", "Speed", "Stealth", "Cunning"]
    ability_level = {}
    new_card = {}

    # Asking user to enter monster card name with character checker
    card_name = char_boundary(1, 20,
                              "Please enter your chosen Monster Card name: ",
                              "Card Name")

    # Loop for the 4 attributes
    for item in attributes:
        # Asking user to enter how much strength card has
        number = easygui.integerbox(f"What is {card_name}'s level of {item}? \n"
                                    f"(Number between 1 and 25) \n",
                                    f"{item}", upperbound=25,
                                    lowerbound=1)

        # Adding items and number to as the ability
        ability_level[item] = number

    # Adding ability's and monster card name to a new dictionary
    new_card[card_name] = ability_level

    # Joinning code for monster cards dictionary
    new_card_formatted = joinning(new_card)

    # Output results and asking if correct results
    answer = easygui.buttonbox("The new Monster Card is: \n\n"
                               f"{new_card_formatted} \n\n"
                               f"Is this new Monster Card correct?",
                               choices=["Yes", "No"])

    # User enters yes
    if answer == "Yes":
        easygui.msgbox("Great! This New Combo was added", "New Combo Added")
        monster_cards.update(new_card)
        print(monster_cards)

    # User enters no
    elif answer == "No":
        easygui.msgbox("So Sorry! Lets make some changes",
                       "New Card incorrect")


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
        easygui.msgbox("Goodbye! Thanks for using Monster Cards",
                       "Leaving Screen")
        break
