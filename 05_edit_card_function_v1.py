""" Component 3 -- Edit card function (version 1)
Adding char_boundry for changing name
Adding a number boundry on level entry so
number between 1 and 25
Converting into a recyclable function
Adding upper and lower boundary on integer
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


# A monster card
monster_card = {
    "Stoneling":
        {"Strength": 7,
         "Speed": 1,
         "Stealth": 25,
         "Cunning": 15},
}

# Calling on edit function
edit(monster_card)

# Output Monster cards
print(joinning(monster_card))
