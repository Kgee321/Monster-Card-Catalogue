""" Component 3 -- Edit card (version 4)
Trial 3
Doesn't use a single loops to change attribute
level.
This is because only 1 card being used so
doesn't need a loop to access the card.
Shortest and most efficient code
This code will be used in my future program.
Written by Katelyn
Created on the 7/05/2023
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


# A monster card
edit_card = {
    "Stoneling":
        {"Strength": 7,
         "Speed": 1,
         "Stealth": 25,
         "Cunning": 15},
}

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
        edit_name = easygui.enterbox("Enter the new card name: ",
                                     "Editing card name").title()

        # Adding name change to final dictionary
        edit_card[edit_name] = edit_card.pop(original_name)

    else:

        # Asking for new level
        edit_level = easygui.integerbox(f"Enter the new level of {what_edit}",
                                        f"{what_edit} new level")

        # Adding level change
        edit_card[original_name][what_edit] = edit_level
