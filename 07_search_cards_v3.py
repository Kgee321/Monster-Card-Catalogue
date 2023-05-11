""" Component 4 -- Search Cards (version 3)
Trial 2 -- Boolean variable
Same code as search_cards_v2 but uses a boolean
to find if search not in monster cards
This code a little shorter and simpler than trial 1
This code will be used in the future program
Written by Katelyn Gee
Created on the 10/05/2023
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

# Variable setting
value = True

# User enters search
searching = input("What Monster Card are you looking for? ").title()

# Loop to access all dictionary items
for name_card, item_card in monster_cards.items():

    # If search is in monster card name
    if searching in name_card:
        print(f"The Monster Card named {name_card} has {item_card}")
        value = False

# Warning message if search not in monster cards
if value:
    print("Sorry, input not a Monster Card")
