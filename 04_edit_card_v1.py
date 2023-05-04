""" Component 3 -- Edit card (version 1)
Adding a monster card into use as card to edit
Code should ask what player wants to edit
Going straight to using easygui as it will
be hard and unnecessary to use print statements
for asking what part of the card they want to
edit.
Adding the joinning function so dictionary can be printed
Written by Katelyn Gee
Created on the 4/05/2023
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

# Calling on join function
edit_card_formatted = joinning(edit_card)

# Asking what user wants to edit
what_edit = easygui.buttonbox("What part of this card would you like to edit: \n"
                              f"{edit_card_formatted}", "Editing card",
                              choices=["Name", "Strength", "Speed",
                                       "Stealth", "Cunning",
                                       "Nothing: This card is correct"])


for edit_name, edit_values in edit_card.items():

    # Changing name
    if what_edit == "Name":

        # Asking what user want to change name to
        edit_name = easygui.enterbox("Enter the new card name: ",
                                     "Editing card name")

        # Changing name in combo
        edit_card[edit_name] = edit_values
