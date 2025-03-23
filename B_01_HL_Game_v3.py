import math
import random


def int_check(question, error, blank, bigger_than, smaller_than, exit_enabled="no"):
    """Checks if the user has entered an integer"""

    while True:

        response = input(question)

        if exit_enabled == "yes" and response == "xxx":
            return response

        if response == "":
            return blank

        try:
            response = int(response)
            if smaller_than == "none":
                if response < bigger_than:
                    print(error)
                else:
                    return response
            else:
                if response < bigger_than or response > smaller_than:
                    print(error)
                else:
                    return response

        except ValueError:
            print(error)


def string_checker(question, valid_ans=("yes", "no")):
    """Asks the user for an answer (from a list)"""

    error = f"Please enter a value from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it is lowercase
        user_response = input(question).lower()

        for i in valid_ans:
            # check if the user response is a word in the list
            if i == user_response:
                return i
            # check if the user response
            # the first letter of an item in the list
            elif user_response == i[0]:
                return i

        # print error if user does not enter something valid
        print(error)
        print()


def instructions():
    """Prints instructions."""

    print('''***** Instructions *****

To begin, choose the range you want to guess from (or press 
<enter> for 1 and 100) and choose the number of rounds (or 
press <enter> for infinite rounds).

Then you can start guessing to find the hidden number in 
that range without running out of guesses!

Enter <xxx> to exit at anytime.

Good luck!
    ''')


def calc_guesses(low, high):
    """Calculates the number of guesses allowed"""

    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


def no_duplicates(number, guessed_list):
    """Checks if the number has already been guessed"""

    if number not in guessed_list:
        return "no"
    else:
        return "yes"


# sets up some variables
rounds_played = 0
guesses_used = 0
num_won = 0
end_game = "no"

# list to hold the outcome of each round
game_history = []

# list to hold all users scores and make finding statistics easy
all_scores = []

# prints title
print("🔼🔼🔼 Higher or Lower 🔽🔽🔽")

# instructions
want_instructions = string_checker("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()

# ask for low parameter (or <enter> for 1)
low_parameter = int_check("What is the the low parameter (or press <enter> for 1)? ", "Please enter an integer that is "
                                                                                      "1 or more, or press <enter> for "
                                                                                      "1", 1, 1, "none")

# ask for high parameter (or <enter> for 100)
high_parameter = int_check("What is the the high parameter (or press <enter> for 100)? ", "Please enter an integer that"
                                                                                          " is higher than "
                                                                                          f"{low_parameter}, or press "
                                                                                          "<enter> for 100",
                           100, low_parameter + 1, "none")
guesses_allowed = calc_guesses(low_parameter, high_parameter)
print(f"You get {guesses_allowed} guesses per round.")

# ask for rounds (or <enter> for infinite mode)
mode = "regular"
round_num = int_check("How many rounds do you want to play (or press <enter> for infinite)? ", "Please enter an integer"
                                                                                               " that is 1 or more, or "
                                                                                               "press <enter> for "
                                                                                               "infinite.", "infinite",
                      1, "none")

# Sets up infinite mode if necessary
if round_num == "infinite":
    mode = "infinite"

# Game loop starts here
while True:
    guessed = []
    round_won = "no"

    # Checks if enough rounds have been played
    if rounds_played == round_num:
        break

    # Rounds headings (based on mode)
    if mode == "regular":
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {round_num} 💿💿💿"
    else:
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite mode) ♾️♾️♾️"

    print(rounds_heading)
    print()

    # Choose random number between parameters that were set by the user
    secret_num = random.randint(low_parameter, high_parameter)
    print(secret_num)

    while guesses_used < guesses_allowed:
        # Gets user guess, checks it's an integer between the high and low number
        user_choice = int_check("Choose: ", f"Enter an integer inbetween the parameters ({low_parameter} & "
                                            f"{high_parameter} inclusive)", "none", low_parameter, high_parameter,
                                "yes")

        # Checks users don't enter a number that has already been guessed
        double_answer = no_duplicates(user_choice, guessed)

        if user_choice == "none":
            print(f"Enter an integer inbetween the parameters ({low_parameter} & {high_parameter} inclusive)")

        # if the user enters the exit code, break the loop
        elif user_choice == "xxx":
            end_game = "yes"
            break

        # checks if the user has used this answer before
        elif double_answer == "yes":
            print("You hae already guessed this number before, try again.")

        # Checks if the number is lower or higher
        elif user_choice > secret_num:
            print("Lower")
            guesses_used += 1
            guessed.append(user_choice)

        elif user_choice < secret_num:
            print("Higher")
            guesses_used += 1
            guessed.append(user_choice)

        # Check if the answer is guessed first try
        elif user_choice == secret_num and guesses_used == 0:
            guesses_used += 1
            round_won = "yes"
            break

        # Check if correct number is guessed
        else:
            guesses_used += 1
            round_won = "yes"
            break

    # check if the user wants to exit
    if end_game == "yes":
        break

    # Gets game results and adds it to list of history
    if round_won == "yes" and guesses_used == 1:
        round_status = "won"
        num_won += 1
        round_feedback = "🍀🍀🍀 Lucky! You guessed the number first try! 🍀🍀🍀"

    elif round_won == "yes":
        round_status = "won"
        num_won += 1
        round_feedback = f"You {round_status}! | The secret number was {secret_num} | " \
                         f"You got it in {guesses_used} guesses!"

    else:
        round_status = "lost"
        round_feedback = f"You {round_status}! | The secret number was {secret_num} | " \
                         f"You ran out of guesses ({guesses_allowed})!"

        # If users run out of guesses, penalise them by increasing the number of guesses
        guesses_used = guesses_allowed + 2

    print(round_feedback)
    if round_won == "yes" and guesses_used == 1:
        round_feedback = f"You {round_status}! | The secret number was {secret_num} | " \
                          "You got it in 1 guess!"

    # Add feedback to history list and add guesses used to all_scores (for stats)
    history_item = f"Round: {rounds_played + 1} - {round_feedback}"
    game_history.append(history_item)
    all_scores.append(guesses_used)

    rounds_played += 1
    guesses_used = 0

if rounds_played == 0:
    print("🐔🐔🐔 Oh no! You've chickened out! 🐔🐔🐔")

else:

    # calculate stats

    # Get the percentage of rounds won
    percent_won = num_won / rounds_played * 100

    # sorts scores from lowest to highest
    all_scores.sort()

    # First item in sorted list (lowest score)
    best = all_scores[0]

    # Last item in sorted list (worst score)
    worst = all_scores[-1]

    # average (sum of scores divided by number of scores)
    average = sum(all_scores) / len(all_scores)
    print()
    print("📊📊📊 Statistics 📊📊📊")
    print(f"Rounds won: {num_won} ({percent_won:.2f}%)    |   Best score: {best}  |   Worst score: {worst}\n")

    # see history if wanted
    see_history = string_checker("\n🛖🛖🛖 Do you want to see the game history 🛖🛖🛖? ")
    if see_history == "yes":
        print("Game History")

        for item in game_history:
            print(item)
