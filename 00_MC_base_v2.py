""" Base Component -- Version 2
Adding components 5 and 6
Replacing function search() with search_delete()
so one function can delete and search function.
Replacing the joinning function with the output
cards function throughout code.
Written by Katelyn Gee
Created on the 21/05/2023
"""

import easygui


# Function for checking characters stay in letter boundary
def char_boundary(lower, upper, question_message, box):
    # Loop for character checker
    while True:
        # Asking user to enter monster card name
        question = easygui.enterbox(question_message, box)

        # Cancel button entered
        if not question:
            easygui.msgbox("Wrong Input. Filed requires an answers",
                           "No answer")

        # Upper string boundary
        elif len(question) > upper:
            easygui.msgbox("Wrong Input. Please enter less than 20 letters",
                           "Number to high")

        # Lower string boundary
        elif len(question) < lower:
            easygui.msgbox("Wrong Input. Please more than 1 letters",
                           "Number to low")

        # Input correct
        else:
            return question.title()


# Function for adding a new Monster Card
def add():

    # Variable setting
    attributes = ["Strength", "Speed", "Stealth", "Cunning"]
    ability_level = {}
    new_card = {}

    # Asking user to enter monster card name with character checker
    card_name = char_boundary(1, 20,
                              "Please enter your chosen Monster Card name: ",
                              "Card Name")

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
    new_card_formatted = output_cards("--", new_card)

    # Output results and asking if correct results
    answer = easygui.buttonbox("The new Monster Card is: \n"
                               f"{new_card_formatted} \n"
                               f"Is this new Monster Card correct?",
                               choices=["Yes", "No"])

    # User enters no
    if answer == "No":
        easygui.msgbox("So sorry. Lets make some changes!",
                       "New Card incorrect")
        edit(new_card)

    # Adding new card
    else:
        monster_cards.update(new_card)

    # Card being added
    easygui.msgbox("Great! This New Card was added",
                   "New card Added")


# Function to edit a card
def edit(edit_card):

    # Loop for editing the card
    while True:

        # Formatted dictionary
        edit_card_format = output_cards("--", edit_card)

        # Asking what user wants to edit
        what_edit = easygui.buttonbox("What part of this card would you like to edit: \n"
                                      f"{edit_card_format}", "Editing card",
                                      choices=["Name", "Strength", "Speed",
                                               "Stealth", "Cunning",
                                               "Exit"])

        # Setting value of the original edit card name
        original_name = next(iter(edit_card))

        # User wants to leave exit card program
        if what_edit == "Exit":
            break

        # Changing name
        elif what_edit == "Name":

            # Asking what user want to change name to
            edit_name = char_boundary(1, 20, "Enter the new card name: ",
                                      "Editing card name")

            # Adding name change to final dictionary
            edit_card[edit_name] = edit_card.pop(original_name)

        else:

            # Asking for new level
            edit_level = easygui.integerbox(f"Enter the new level of {what_edit}",
                                            f"{what_edit} new level",
                                            upperbound=25,
                                            lowerbound=1)

            # Adding level change
            edit_card[original_name][what_edit] = edit_level

    # Adding card to monster cards
    monster_cards.update(edit_card)


# Function for finding cards in monster cards
def search_delete(action, message, other_action):
    while True:
        # Variable setting
        var = True
        cards_in_search = {}

        # User enters search
        searching = char_boundary(1, 20,
                                  f"Enter what you want to {action} in Monster Cards:",
                                  f"{action.title()} Monster Cards")

        # Loop to access all dictionary items
        for name_card, item_card in monster_cards.items():

            # If search is in monster card name
            if searching in name_card:

                # Code knows search is in monster cards
                var = False

                # Adding card to dictionary
                cards_in_search[name_card] = monster_cards[name_card]

        # Warning message if search not in monster cards and code ending
        if var:
            easygui.msgbox("Sorry, input not in Monster Cards",
                           "Not in Monster Cards")
            break

        # Formatting dictionary nicely
        formatted_item = output_cards("--", cards_in_search)

        # Checking if monster card is correct
        correct = easygui.buttonbox(f"Here are the following Monster Cards found: \n"
                                    f"{formatted_item}\n"
                                    f"{message}",
                                    f"Checking Monster Card found",
                                    choices=["Yes", "No"])

        # If card is correct
        if correct == "No":
            easygui.msgbox(f"Ok, no {other_action} has been made to the catalogue", "Card is Correct")
            break

        # If more than 1 search result
        if len(cards_in_search) >= 2:
            card_to_edit = easygui.buttonbox(f"What Monster Card would you like to {other_action}:",
                                             "Choosing a Card",
                                             choices=list(cards_in_search.keys()))
        else:
            card_to_edit = next(iter(cards_in_search))

        # Removing old Monster card
        del monster_cards[card_to_edit]

        # Editing car
        if action == "search":

            # Editing monster card
            edit({card_to_edit: cards_in_search[card_to_edit]})

            # Leaving message
            easygui.msgbox("Ok! Monster card has been changed")
            break

        else:

            # Telling user card has been deleted
            easygui.msgbox(f"{card_to_edit} has been {other_action}d")
            break


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


# Monster Cards Catalogue stored
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

# Welcome and Instructions
easygui.msgbox("Welcome to Monster Card Catalogue! \n"
               "You have the option to add a Card, "
               "search cards, delete a card, "
               "or show all the cards in this program. "
               "Please select what you would "
               "like to do on the next page."
               "\nEnjoy!", "Welcome and Instructions")

# Loop so code ends when user wants it to
while True:

    # Asking user what they want to do with the monster cards
    options = easygui.buttonbox("Enter what you would like to do with "
                                "the Monster Cards: \n",
                                "Home Screen",
                                choices=["Add", "Search", "Delete",
                                         "Print", "Exit"])

    # If user want to add a card
    if options == "Add":
        add()

    # If user wants to find cards
    elif options == "Search":

        # Calling on function to search card
        search_delete("search", "Are any of these card incorrect?", "edit")

    # If user wants to delete a card
    elif options == "Delete":

        # Calling on function to delete card
        search_delete("delete", "Do you want to delete any of these cards?", "delete")

    # If user want to print all cards
    elif options == "Print":

        # Output the monster cards
        print(output_cards("~", monster_cards))

    # If user want to leave code
    elif options == "Exit":

        # Goodbye message outputted and code ends
        easygui.msgbox("Goodbye! Thanks for using Monster Cards",
                       "Leaving Screen")
        break
