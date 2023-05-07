""" Component 3 -- Edit card (version 4)
Trial 3
Use a for in range loop and a separate list
of attributes in order to change the
attributes values.
Code works but is unnecessary long.
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

# Attributes list
attributes = ["Strength", "Speed", "Stealth", "Cunning"]

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

    # If card not changing
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

        # Button if an attribute being changed
        else:

            # Loop for finding changing attribute value
            for num in range(len(attributes)):

                # Attribute being used
                using = attributes[num]

                # If correct attribute found
                if using == what_edit:

                    # Asking for new level
                    edit_level = easygui.integerbox(f"Enter the new level of {using}",
                                                    f"{using} new level")

                    # Adding level change
                    edit_card[original_name][using] = edit_level
                    break

                # If attribute not the one wanting to use
                else:
                    continue
