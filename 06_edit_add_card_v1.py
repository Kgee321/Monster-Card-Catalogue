""" Component 3 -- Edit card function combined with the
add card function (version 1).
In the add card function, code calls on the edit card
function.
Combining the codes from 02_add_card_function_v1
and 05_edit_card_function_v1.
Making changes to add card function to suit
the edit card changes added in.
Removing the ok message in edit card as no longer
necessary and might frustrate the user
Adding the edit() function to base component v1
Adding the add() function to base component v1
Written by Katelyn
Created on the 8/05/2023
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


# Function to edit a card
def edit(edit_card):

    # Loop for editing the card
    while True:

        # Formatted dictionary
        edit_card_format = joinning(edit_card)

        # Asking what user wants to edit
        what_edit = easygui.buttonbox("What part of this card would you like to edit: \n"
                                      f"{edit_card_format}", "Editing card",
                                      choices=["Name", "Strength", "Speed",
                                               "Stealth", "Cunning",
                                               "Exit"])

        # Setting value of the original edit card name
        original_name = next(iter(edit_card))

        # User wants to leave exit card program
        if what_edit == "Exit":

            # Happy message
            easygui.msgbox("Ok!", "Changes complete")
            break

        # Changing name
        elif what_edit == "Name":

            # Asking what user want to change name to
            edit_name = char_boundary(1, 20, "Enter the new card name: ",
                                      "Editing card name")

            # Adding name change to final dictionary
            edit_card[edit_name] = edit_card.pop(original_name)

        else:

            # Asking for new level
            edit_level = easygui.integerbox(f"Enter the new level of {what_edit}",
                                            f"{what_edit} new level",
                                            upperbound=25,
                                            lowerbound=1)

            # Adding level change
            edit_card[original_name][what_edit] = edit_level


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

    # User enters no
    if answer == "No":
        easygui.msgbox("So sorry. Lets make some changes!",
                       "New Card incorrect")
        edit(new_card)

    # Card being added
    easygui.msgbox("Great! This New Combo was added", "New Combo Added")
    monster_cards.update(new_card)


# A monster card
monster_cards = {
    "Stoneling":
        {"Strength": 7,
         "Speed": 1,
         "Stealth": 25,
         "Cunning": 15},
}

# Calling on add card function
add()
