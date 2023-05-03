""" Component 2 -- Add Card (version 1)
Asking the user to add the Card name
Not using Easygui yet but print statements
Asking user to enter a number for each ability
without a loop used so a long line of code.
Written by Katelyn
Created on 2/05/2023
"""

# Asking user to enter monster card name
card_name = input("Please enter your chosen Monster Card name: ").title()

# Asking user to enter how much strength card has
strength = int(input(f"What is {card_name}'s level of strength? \n"
                     f"Enter as a number between 1 and 25 \n"))

# Asking user to enter how much strength card has
speed = int(input(f"What is {card_name}'s level of speed? \n"
                  f"Enter as a number between 1 and 25 \n"))

# Asking user to enter how much strength card has
stealth = int(input(f"What is {card_name}'s level of stealth? \n"
                    f"Enter as a number between 1 and 25 \n"))

# Asking user to enter how much strength card has
cunning = int(input(f"What is {card_name}'s level of cunning? \n"
                    f"Enter as a number between 1 and 25 \n"))

# Output results
print("The new monster card is: \n\n"
      f"{card_name}: \n"
      f"{len(card_name) * '-'} \n"
      f"- Strength is {strength} \n"
      f"- Speed is {speed} \n"
      f"- Stealth is {stealth} \n"
      f"- Cunning is {cunning}")
