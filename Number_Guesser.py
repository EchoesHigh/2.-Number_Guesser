# Module Import
import random

# Variables
str_top_of_range = ""
int_random_number = 0
str_user_guess = ""
int_guesses = 0
int_negative = 0

# Start of the program
print ("Welcome to the Number Guesser game!")
print ("The number you type will be the upper limit number for this game!")
str_top_of_range = input("Type a number: ")

if str_top_of_range.isdigit():                                  # To make sure the user typed a number
    str_top_of_range = int(str_top_of_range)

    if str_top_of_range == 0:                                   # If the user types 0
        print ("Please enter a number greater than 0...")
        quit()

elif str_top_of_range.startswith("-"):                          # If the user types a number lower than 0
    int_negative = str_top_of_range.lstrip("-")                 # Removes the minus symbol
    if int_negative.isdigit():                                  # To make sure the user typed a number
        print ("Please enter a number greater than 0")
        quit()
    else:                                                       # If the user types something different than a number
        print ("Please enter a number")
        quit()

else:                                                           # If the user types something different than a number
    print ("Please enter a number...")
    quit()

int_random_number = random.randint(0, str_top_of_range)         # Generation of the random number based on the user input

while True:
    int_guesses += 1
    str_user_guess = input("Make a guess: ")
    if str_user_guess.isdigit():                                # If the user enters a number
        str_user_guess = int(str_user_guess)
    elif str_user_guess.startswith("-"):                        # If the user types a number lower than 0
        int_negative = str_user_guess.lstrip("-")               # Removes the minus symbol
        if int_negative.isdigit():                              # To make sure the user typed a number
            print ("Please enter a number greater or equal than 0...")
            continue                                            # Jumps to the start of the while
        else:                                                   # If the user types something different than a number
            print ("Please enter a number...")
            continue                                            # Jumps to the start of the while
    else:                                                       # If the user types something different than a number
        print ("Please enter a number...")
        continue                                                # Jumps to the start of the while

    if str_user_guess == int_random_number:                     # If the user guess it
        print ("You got it!")
        break
    elif str_user_guess > int_random_number:                    # If the user guess is greater than the random number
            print ("You were above the number!")
    else:                                                       # If the user guess is lower than the random number
            print ("You were below the number!")

print ("You got it in", int_guesses, "guesses!")                # Shows the total number of attempts
print ("Thank you for playing!")