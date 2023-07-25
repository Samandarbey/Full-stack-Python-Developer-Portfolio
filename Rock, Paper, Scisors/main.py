import random
exit = False
user_points = 0
computer_points = 0
while exit == False:
    options = ["rock","paper","scissors"]
    user_input = input("Choose rock, paper, scissors or exit: ").lower()
    computer_input = random.choice(options)
    if user_input == "exit":
        print("Game Over! ")
        print(f"You won a total score of {user_points} times and computer won a total score of {computer_points} times! ")
        exit = True
        
    if user_input == "rock":
        if computer_input == "rock":
            print("Your input is rock")
            print("Computer input is rock")
            print("It is a tie! ")
            
        elif computer_input == "paper":
            print("Your input is rock")
            print("Computer input is paper")
            print("Computer won! ")
            computer_points += 1
            
        elif computer_input == "scissors":
            print("Your input is rock")
            print("Computer input is scissors")
            print("You won! ")
            user_points += 1
            
            
            
    elif user_input == "paper":
        if computer_input == "rock":
                print("Your input is  paper")
                print("Computer input is rock")
                print("You won! ")
                user_points += 1
            
        elif computer_input == "paper":
                print("Your input is paper")
                print("Computer input is paper")
                print("It is a tie! ")
                # computer_points += 1
                
        elif computer_input == "scissors":
                print("Your input is paper")
                print("Computer input is scissors")
                print("Computer won! ")
                computer_points += 1 
    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input is scissors ")
            print("Computer input is rock")
            print("Computer won! ")
            computer_points += 1
            
        elif computer_input == "paper":
            print("Your input is scissors")
            print("Computer input is paper")
            print("You won! ")
            user_points += 1
            
        elif computer_input == "scissors":
            print("Your input is scissors")
            print("Computer input is scissors")
            print("It is a tie! ")
            # user_points += 1 
            
    elif user_input != "rock" or user_input != "paper" or user_input!="scissors" :
        print("Invalid Option!") 
                
                
                
                
                
                
                      