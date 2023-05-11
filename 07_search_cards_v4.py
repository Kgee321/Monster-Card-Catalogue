""" Component 4 -- Search Cards (version 4)
Adding onto search_cards_v3.
Adding a loop for testing
Adding the char_boundry so input it correct
and for testing purposes
Written by Katelyn Gee
Created on the 10/05/2023
"""


# Function for checking characters stay in letter boundary
def char_boundary(lower, upper, question_message):
    # Loop for character checker
    while True:
        # Asking user to enter monster card name
        question = input(question_message)

        # Upper string boundary
        if len(question) > upper:
            print("Wrong Input. Please enter less than 20 letters")

        # Lower string boundary
        elif len(question) < lower:
            print("Wrong Input. Please more than 1 letters")

        # Input correct
        else:
            return question.title()


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

while True:
    # Variable setting
    value = True

    # User enters search
    searching = char_boundary(1, 20,
                              "What Monster Card are you looking for? ")

    # Loop to access all dictionary items
    for name_card, item_card in monster_cards.items():

        # If search is in monster card name
        if searching in name_card:
            print(f"The Monster Card named {name_card} has {item_card}")
            value = False

    # Warning message if search not in monster cards
    if value:
        print("Sorry, input not a Monster Card")
