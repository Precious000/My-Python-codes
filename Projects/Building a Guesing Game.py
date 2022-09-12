# Building a Guessing Game that prompts users to enter a value
# In this Game we'll ask a user to enter the color of a countries flag
# First we'll save the predefined correct answer in a variable
# Next we'll create an empty variable where the users input will go in
# Then we'll create a guess limit that stops the user from entering more guesses if they fail to enter the correct guess

# LET'S GO!
Correct_Answer = "Green and white"
Guess = ""
number_of_guesses = 0
Guess_limit = 3
while Guess != "Green and white":
    if number_of_guesses < 3:
        Guess = input("Enter the color of Nigeria flag: ")
        number_of_guesses += 1
    else:
        number_of_guesses = 3
        print("You loose!")
        break

print("You win!")
