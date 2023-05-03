""" Component 2 -- Add Card (version 3)
Trial 1 -- Integer checker
Converting code into easygui
Adding an integer checker so user
can only enter correct input and code
doesn't crash.
This code is not used in the future program
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

    # Loop for testing if input an integer
    while True:

        try:
            # Asking user to enter how much strength card has
            number = int(easygui.enterbox(f"What is {card_name}'s level of {item}? \n"
                                      f"Enter as a number between 1 and 25 \n",
                                      f"{item}"))

            # Number is bigger than 25
            if number > 25:
                easygui.msgbox("Sorry, number is to big. Try again", "Number too High")

            # Number smaller 1
            elif number < 1:
                easygui.msgbox("Sorry, number is to small. Try again", "Number too Low")

            # Correct input
            else:
                break

        # If code crash as wrong input
        except ValueError:
            easygui.msgbox("Sorry, wrong input. Please enter an integer")

    # Adding items and number to dictionary
    monster_cards[item] = number

# Output results
print("The new monster card is: \n\n"
      f"{card_name}: \n"
      f"{len(card_name) * '-'} \n"
      f"{monster_cards}")
