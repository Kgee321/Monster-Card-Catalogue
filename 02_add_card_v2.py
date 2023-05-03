""" Component 2 -- Add Card (version 2)
Use loops to simplify code
Put the different attributes into a list
Appending the inputs into a dictionary
Written by Katelyn
Created on 2/05/2023
"""

attributes = ["Strength", "Speed", "Stealth", "Cunning"]
monster_cards = {}

# Asking user to enter monster card name
card_name = input("Please enter your chosen Monster Card name: ").title()

# Loop for the 4 attributes
for item in attributes:

    # Asking user to enter how much strength card has
    number = int(input(f"What is {card_name}'s level of {item}? \n"
                       f"Enter as a number between 1 and 25 \n"))

    # Adding items and number to dictionary
    monster_cards[item] = number

# Output results
print("The new monster card is: \n\n"
      f"{card_name}: \n"
      f"{len(card_name) * '-'} \n"
      f"{monster_cards}")
