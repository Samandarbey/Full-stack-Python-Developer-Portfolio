import random

user_wins = 0
computer_wins = 0
step = 0

options = ["rock","paper","scissors"]
# options[0]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        print(f"Final Results You -> {user_wins} score : Computer -> {computer_wins} score")
        quit()



    if user_input not in options :
        continue

    random_number = random.randint(0,2)
    #rock:0, paper: 1, scissors:2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won!")
        user_wins += 1
        # step += 1
        print("You won ", user_wins, "times.")

        continue

    elif user_input == "paper" and computer_pick == "rock":
        print("You Won!")
        user_wins += 1
        # step += 1
        print("You won ", user_wins, "times.")
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1
        # step += 1
        print("You won ", user_wins, "times.")
        continue

    else:
        print("You lost!")
        while True:
            computer_wins += 1
            print("Computer won ", computer_wins, "times.")
            break

        # computer_wins += 1
        # step += 1

print("You won ",user_wins, "times.")
print("Computer won ", computer_wins,"times.")
print("Good Bye!")
#
# if user_input == "q":
#
#     quit()




