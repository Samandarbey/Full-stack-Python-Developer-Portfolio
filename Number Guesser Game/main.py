import random

top_of_range = input("Type a number: ")
guesses = 0


if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("Please type a larger  number than zero")
        quit()
else:
        print("Type a number  next time")

random_number = random.randint(0, top_of_range)


while True:
    guesses += 1
    user_guess = input("make a guess")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Plase type a number next time")
        continue
    if user_guess==random_number:
        print("You got it")
        break
    else:
        # print("You got it wrong!")

        if user_guess > random_number:
            print("you are above the number")
        else:
            print("you were below the number")
print("you got it in", guesses, "guesses")

