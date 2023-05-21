""" Component 6 -- Output Menu (version 3)
Changed the Deco so that it is more fun and creative
Tested this code against version 2 and agreed that
this code is more fun and relevant to my audience.
This code will be used in future program.
Written by Katelyn
Created on the 21/05/2023
"""

# Pre Stored Monster Cards dictionary
monster_cards = {
    "Stoneling":
        {"Strength": 7,
         "Speed": 1,
         "Stealth": 25,
         "Cunning": 15},
    "Vexscream":
        {"Strength": 1,
         "Speed": 6,
         "Stealth": 21,
         "Cunning": 19},
    "Dawnmirage":
        {"Strength": 5,
         "Speed": 15,
         "Stealth": 18,
         "Cunning": 22},
    "Blazegolem":
        {"Strength": 15,
         "Speed": 20,
         "Stealth": 23,
         "Cunning": 6},
    "Websnake":
        {"Strength": 7,
         "Speed": 15,
         "Stealth": 10,
         "Cunning": 5},
    "Moldvine":
        {"Strength": 21,
         "Speed": 18,
         "Stealth": 14,
         "Cunning": 5},
    "Vortexwing":
        {"Strength": 19,
         "Speed": 13,
         "Stealth": 19,
         "Cunning": 2},
    "Rotthing":
        {"Strength": 16,
         "Speed": 7,
         "Stealth": 4,
         "Cunning": 12},
    "Froststep":
        {"Strength": 14,
         "Speed": 14,
         "Stealth": 17,
         "Cunning": 4},
    "Wispghoul":
        {"Strength": 17,
         "Speed": 19,
         "Stealth": 3,
         "Cunning": 2}
}

message = ""

# loop to print dictionary
for name_of_card, card_items in monster_cards.items():

    # Card name added
    message += f"\n{name_of_card}\n"
    message += f"~" * (len(name_of_card)) + f"\n"

    # Loop to print dictionary inside the dictionary
    for item_in_card, level_of_item in card_items.items():

        # Card item and its level added
        message += f" ~ {item_in_card}: {level_of_item} \n"

print(message)
