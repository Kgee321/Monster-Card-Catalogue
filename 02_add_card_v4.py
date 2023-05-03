""" Component 2 -- Add Card (version 4)
Trial 2 -- Integer box
Using an easygui integerbox to check if
an integer is entered.
Creating number boundary in the integerbox
Much shorter code than Trial 1
This code will be used in the future program
Written by Katelyn
Created on 2/05/2023
"""

import easygui

attributes = ["Strength", "Speed", "Stealth", "Cunning"]
monster_cards = {}

# Asking user to enter monster card name
card_name = easygui.enterbox("Please enter your chosen Monster Card name: ").title()

# Loop for the 4 attributes
for item in attributes:
    # Asking user to enter how much strength card has
    number = easygui.integerbox(f"What is {card_name}'s level of {item}? \n"
                                f"Enter as a number between 1 and 25 \n",
                                f"{item}", upperbound=25,
                                lowerbound=1)

    # Adding items and number to dictionary
    monster_cards[item] = number

# Output results
print("The new monster card is: \n\n"
      f"{card_name}: \n"
      f"{len(card_name) * '-'} \n"
      f"{monster_cards}")
