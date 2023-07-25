import random 

def roll_dice():
    
    roll = input("Roll the dice? (Yes/No): ")
    while roll.lower() == "Yes".lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        
        print("Dice rolled: {} and {}".format(dice1, dice2))
        
        roll = input("Roll again? (Yes/No) ")
        if roll == "No".lower():
            print("Thanks for using this programm, Hopefully it was enjoyable! ")
            
            
            
            
            
            break
        else:
            continue


        
# roll_dice()

game = input("We have really funny game for you which is called Dice Rolling! Do you wanna play? (yes/no)\n ").lower()
if game == "yes":
    print("Let's start  the game! ")
    roll_dice()
else:
    print("OK think again bro! ")
    quit()

    