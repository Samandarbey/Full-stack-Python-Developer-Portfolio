from random import *
def say():
    ask = input("What do you want I reply your sentence!")
    print(ask)
    ask2 = input("did you say this? (yes/no) \n").lower()
    if ask2 == "yes":
        print("Thanks! Good!") 
    else:
        print("Write once more time, please! ")
# say()
while True:
    answer = input("Are you ready? (yes/no)\n").lower()
    if answer == "yes":
        print("OK, let's get started! \n")
        say()
    elif answer == "no":
        print("OK, Let's quit this program! \n")
        quit()
    else:
        print("Invalid option, please enter 'yes' or 'no' \n" )
        continue