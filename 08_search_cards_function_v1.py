""" Component 4 -- Search Cards Function (version 1)
Changing main code into a function.
Adding in Joinning function
Changing char_boundary function so that
it uses easygui
Written by Katelyn Gee
Created on the 11/05/2023
"""


# Function for joinning dictionary's
def joinning(dic):
    message = ""

    # Joinning the dictionary inputted
    for key, value in dic.items():
        message += f"{key}:\n"

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


