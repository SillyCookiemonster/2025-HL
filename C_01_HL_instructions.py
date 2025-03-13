# functions go here

# Check that users have entered a valid
# option based on a list
def string_checker(question, valid_ans=("yes", "no")):
    error = f"Please enter a value from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it is lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word in the list
            if item == user_response:
                return item
            # check if the user response
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter something valid
        print(error)
        print()


def instructions():
    """Prints instructions."""

    print('''***** Instructions *****

To begin, choose the range you want to guess from (or press 
<enter> for 0 to 100) and choose the number of rounds (or 
press <enter> for infinite rounds).

Then you can start guessing to find the hidden number in 
that range without running out of guesses!

Enter <xxx> to exit at anytime.

Good luck!
    ''')


# Main routine


want_instructions = string_checker("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()

print("program continues")
