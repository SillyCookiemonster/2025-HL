import math
import random


def int_check(question, error, blank, bigger_than, smaller_than, exit_enabled="no"):
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
<enter> for 0 to 100) and choose the number of rounds (or 
press <enter> for infinite rounds).

Then you can start guessing to find the hidden number in 
that range without running out of guesses!

Enter <xxx> to exit at anytime.

Good luck!
    ''')


# calculate the number of guesses allowed
def calc_guesses(low, high):
    num_range = high - low + 1
    max_raw = math.log2(num_range)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    return max_guesses


def no_duplicates(number, guessed_list):
    if number not in guessed_list:
        return "no"
    else:
        return "yes"


rounds_played = 0
guesses_used = 0
end_game = "no"

game_history = []

print("🔼🔼🔼 Higher or Lower 🔽🔽🔽")

# instructions
want_instructions = string_checker("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()

# ask for low parameter
low_parameter = int_check("What is the the low parameter (or press <enter> for 1)? ", "Please enter an integer that is "
                                                                                      "1 or more, or press <enter> for "
                                                                                      "1", 1, 1, "none")

# ask for high parameter and make 100 if empty
high_parameter = int_check("What is the the high parameter (or press <enter> for 100)? ", "Please enter an integer that"
                                                                                          " is higher than "
                                                                                          f"{low_parameter}, or press "
                                                                                          "<enter> for 100",
                           100, low_parameter + 1, "none")
guesses_allowed = calc_guesses(low_parameter, high_parameter)
print(guesses_allowed)

# ask for rounds (or <enter> for infinite mode)
mode = "regular"
round_num = int_check("How many rounds do you want to play (or press <enter> for infinite)? ", "Please enter an integer"
                                                                                               " that is 1 or more, or "
                                                                                               "press <enter> for "
                                                                                               "infinite.", "infinite",
                      1, "none")

if round_num == "infinite":
    mode = "infinite"

# Game loop starts here
while True:
    guessed = []

    if rounds_played == round_num:
        break

    # Rounds headings (based on mode)
    if mode == "regular":
        rounds_heading = f"\n💿💿💿 Round {rounds_played + 1} of {round_num} 💿💿💿"
    else:
        rounds_heading = f"\n♾️♾️♾️ Round {rounds_played + 1} (Infinite mode) ♾️♾️♾️"

    print(rounds_heading)
    print()

    secret_num = random.randint(low_parameter, high_parameter)
    print(secret_num)

    for item in range(0, guesses_allowed):
        # gets user choice
        user_choice = int_check("Choose: ", f"Enter an integer inbetween the parameters ({low_parameter} & "
                                            f"{high_parameter} inclusive)", "none", low_parameter, high_parameter,
                                "yes")

        if user_choice == "none":
            print(f"Enter an integer inbetween the parameters ({low_parameter} & {high_parameter} inclusive)")

        # if the user enters the exit code, break the loop
        elif user_choice == "xxx":
            end_game = "yes"
            break

        elif user_choice == secret_num and guesses_used == 0:
            print("Lucky! You guessed the number first try!")
            break

        elif user_choice == secret_num:
            print(f"You guessed the secret number in {guesses_used}!")
            break

        elif isinstance(user_choice, int):
            double_answer = no_duplicates(user_choice, guessed)
            if double_answer == "no":
                print("that wasn't a duplicate")
                guessed.append(user_choice)
                guesses_used += 1
                if user_choice > secret_num:
                    print("Lower")
                elif user_choice < secret_num:
                    print("Higher")
                else:
                    print("you won!")
                pass
            else:
                print("that was a duplicate")
                pass

    if end_game == "yes":
        break

    rounds_played += 1
    guesses_used = 0

print("game finished")
