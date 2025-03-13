def int_check(question, error):
    while True:

        response = input(question)

        if response == "":
            return "infinite"

        try:
            response = int(response)

            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


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


print("🔼🔼🔼 Higher or Lower 🔽🔽🔽")

# instructions
want_instructions = string_checker("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()

# ask for rounds (or <enter> for infinite mode)
rounds_played = 0
mode = "regular"
round_num = int_check("How many rounds do you want to play? ", "Please enter an integer that is 1 or more, or press "
                                                               "<enter> for infinite.")

if round_num == "infinite":
    mode = "infinite"

# Game loop starts here
while True:

    if rounds_played == round_num:
        break

    # Rounds headings (based on mode)
    if mode == "regular":
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {round_num} 💿💿💿"
    else:
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite mode) ♾️♾️♾️"

    print(rounds_heading)
    print()

    # gets user choice
    user_choice = input("Choose: ")

    # if the user enters the exit code, break the loop
    if user_choice == "xxx":
        break

    rounds_played += 1

print("game finished")
