""" Component 2 -- Add Card Function (version 1)
Convert code into a recyclable function
where appropriate.
Also put the joinning the dictionary into
a recyclable function
Also another function for character checking and
making sure code works if cancel button entered
Making sure all easygui boxes are named
Written by Katelyn
Created on 3/05/2023
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
        question = easygui.enterbox(question_message, box)

        # Cancel button entered
        if not question:
            easygui.msgbox("Wrong Input. Filed requires an answers",
                           "No answer")

        # Upper string boundary
        elif len(question) > upper:
            easygui.msgbox("Wrong Input. Please enter less than 20 letters",
                           "Number to high")

        # Lower string boundary
        elif len(question) < lower:
            easygui.msgbox("Wrong Input. Please more than 1 letters",
                           "Number to low")

        # Input correct
        else:
            return question.title()


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

        easygui.msgbox("Great! This New Card was added", "New Card Added")
        monster_cards.update(new_card)

    # User enters no
    elif answer == "No":
        easygui.msgbox("So sorry. Lets make some changes!",
                       "New Card incorrect")


# All monster cards
monster_cards = {}

# Calling on add new card function
add()

# Printing card for testing
print(monster_cards)
