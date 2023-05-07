""" Component 3 -- Edit card (version 2)
Trial 1
Adding in other 4 attribute buttons using
another for loop.
Code works well but quite long.
Adding in Joinning function for neat dictionary
Written by Katelyn
Created on the 5/05/2023
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

        # Loop to allow access to card level
        for original_attribute, original_level in original_value.items():

            # if changing strength
            if what_edit == original_attribute:

                # Asking for new level
                edit_level = easygui.integerbox(f"Enter the new level of {original_attribute}",
                                                f"{original_attribute} new level")

                # Changing new level
                edit_card[original_name][original_attribute] = edit_level

                break

    # If card not changing
    if what_edit == "Exit":

        # Happy message
        easygui.msgbox("Ok!", "Changes complete")
        break
