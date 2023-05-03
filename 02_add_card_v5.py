""" Component 2 -- Add Card (version 4)
Asks user if the new card is correct
Creating a join statement so dictionary
output looks neat
Put a character boundry on name
Written by Katelyn
Created on 2/05/2023
"""

import easygui

# Variable setting
message = ""
attributes = ["Strength", "Speed", "Stealth", "Cunning"]
monster_cards = {}
ability_level = {}
new_card = {}

# Loop for character checker
while True:
    # Asking user to enter monster card name
    card_name = easygui.enterbox("Please enter your chosen Monster Card name: ").title()

    # Upper string boundary
    if len(card_name) > 20:
        easygui.msgbox("Wrong Input. Please enter less than 20 letters")

    # Lower string boundary
    elif len(card_name) < 1:
        easygui.msgbox("Wrong Input. Please more than 1 letters")

    # Input correct
    else:
        break

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
for key, value in new_card.items():
    message = f"{key}:\n"

    # Formatting dictionary inside dictionary
    for key2, value2 in value.items():
        message += f"- {key2}: {value2} \n"

# Output results and asking if correct results
answer = easygui.buttonbox("The new Monster Card is: \n\n"
                           f"{message} \n\n"
                           f"Is this new Monster Card correct?",
                           choices=["Yes", "No"])

# User enters yes
if answer == "Yes":
    easygui.msgbox("Great! This New Combo was added", "New Combo Added")
    monster_cards.update(new_card)
    print(monster_cards)

# User enters no
elif answer == "No":
    easygui.msgbox("Goes to edit card function", "New Card added incorrect")
