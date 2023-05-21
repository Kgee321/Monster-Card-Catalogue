""" Component 5 -- Delete Cards (version 2)
Adding in the edit function to make sure function is still working for
the search function.
Testing both search and delete work for the same code.
Making changes to code where suited
This is the final code and search_delete() function is added to
MC_base_v2.
Written by Katelyn
Created on 17/05/2023
"""

import easygui


# Function for joinning dictionary's
def joinning(dic):
    message = ""

    # Joinning the dictionary inputted
    for key, value in dic.items():
        message += f"\n{key}:\n"

        # Formatting dictionary inside dictionary
        for key2, value2 in value.items():
            message += f"- {key2}: {value2} \n"

    return message


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


# Function to edit a card
def edit(edit_card):

    # Loop for editing the card
    while True:

        # Formatted dictionary
        edit_card_format = joinning(edit_card)

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

    # Updating monster cards with edited card
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
        formatted_item = joinning(cards_in_search)

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

        # Editing car
        if action == "search":

            # Removing old Monster card
            del monster_cards[card_to_edit]

            # Editing monster card
            edit({card_to_edit: cards_in_search[card_to_edit]})

            # Leaving message
            easygui.msgbox("Ok! Monster card has been changed")

            break

        else:

            # Deleting monster card
            del monster_cards[card_to_edit]

            # Telling user card has been deleted
            easygui.msgbox(f"{card_to_edit} has been {other_action}d")
            break


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

# Calling on function to delete card
search_delete("delete", "Do you want to delete any of these cards?", "delete")

# Calling on function to search card
search_delete("search", "Are any of these card incorrect?", "edit")

# Output dictionary to check that the program did delete card
print(joinning(monster_cards))

