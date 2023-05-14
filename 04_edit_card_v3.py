""" Component 3 -- Edit card (version 3)
Trial 2
Using an if statement and else so user can change
the attribute values. Code is significantly
shorter than the 1st trial but still uses
an unnecessary loop.
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
    # User wants to leave exit card program
    if what_edit == "Exit":

        # Happy message
        easygui.msgbox("Ok!", "Changes complete")
        break

    # Loop for access dictionary values
    for original_name, original_value in edit_card.items():

        # Changing name
        if what_edit == "Name":

            # Asking what user want to change name to
            edit_name = easygui.enterbox("Enter the new card name: ",
                                         "Editing card name").title()

            # Adding name change to final dictionary
            edit_card[edit_name] = original_value

            # Deleting old card and ending loop
            del edit_card[original_name]
            break

        else:

            # Asking for new level
            edit_level = easygui.integerbox(f"Enter the new level of {what_edit}",
                                            f"{what_edit} new level")

            # Adding level change
            edit_card[original_name][what_edit] = edit_level
