""" Component 6 -- Output Menu (version 3)
Converted code from version 3 into a
recyclable function for other parts of my code
and so pattern and dictionary can be easily changed.
This is the final code for this section and is added to
MC_base_v2.
This code will be replacing the joinning function I
created earlier.
Written by Katelyn
Created on the 21/05/2023
"""


# Function for connecting dictionaries to be printable
def output_cards(pattern, dictionary):

    message = ""

    # loop to print dictionary
    for name_of_card, card_items in dictionary.items():

        # Card name added
        message += f"\n{name_of_card}\n"
        message += f"{pattern}" * (len(name_of_card)) + f"\n"

        # Loop to print dictionary inside the dictionary
        for item_in_card, level_of_item in card_items.items():

            # Card item and its level added
            message += f"{pattern} {item_in_card}: {level_of_item} \n"

    return message


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

# Output the monster cards
cards_formatted = output_cards("~", monster_cards)
print(cards_formatted)
