""" Component 3 -- Edit card (version 1)
Adding a monster card into use as card to edit
Code should ask what player wants to edit
Going straight to using easygui as it will
be hard and unnecessary to use print statements
for asking what part of the card user wants to
edit.
Starting by only using name and nothing button
Written by Katelyn Gee
Created on the 4/05/2023
"""

import easygui

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

    # Asking what user wants to edit
    what_edit = easygui.buttonbox("What part of this card would you like to edit: \n"
                                  f"{edit_card}", "Editing card",
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

    # If card not changing
    if what_edit == "Exit":
        # Happy message
        easygui.msgbox("Ok!", "No changes needed")
        break
