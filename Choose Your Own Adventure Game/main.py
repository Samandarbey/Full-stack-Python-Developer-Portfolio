name = input("Enter your name: ").title()
print("Welcome", name, "to this adventure!")

answer = input("You are in a dirt road, it has come to an end  you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, Type walk to walk, swim to swim!").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, run out of water and you lost the game")
    else:
        print("Not a valid option.You lose!")
elif answer == "right":
    answer = input("You come to a bridge, it looks wobbly, do you wanna across it or head back (cross/back? ) ")
    if answer == "back":
        print("You go back to the main road and lose!. ")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a strangers. Do you talk to them? (yes/no?)")
        if answer =="yes":
            print("You talk to the strangers and they give you gold and You Win! ")
            print("Do you wanna get this golds? (yes/no?) ")
            if answer == "yes":
                print("You have received these golds. Do you wanna exchange them into virtual money? Enter yes/no ")
                if answer == "yes":
                    print(input("Which currency you want to exchange? ($ or UZS) "))
                    if answer == "$":
                            print("1gramm Gold equels to $50 ")
                            print("How much kilo Gold you have right now to exchange? (e.x -> 100kg")
                            currency = input("Enter kilos of your gold to exchange")
                            # print(f"We have exchanged your {currency} gold into {currency * 50000} $")
                            # print("You Won!")
                            
                            def currency_changer():
                                print(f"We have exchanged your {currency} gold into {currency * 50000} $")
                                print("You Won!")
                                return()
                            print(currency_changer)
                            
                    elif answer == "UZS":
                            print("1gramm Gold equels to 500000 UZS ")
                            print("How much kilo Gold you have right now to exchange? (e.x -> 100kg")
                            currency = input("Enter kilos of your gold to exchange")
                            def currency_changer():
                                print(f"We have exchanged your {currency} gold into {currency * 500000000} UZS")
                                print("You Won!")
                                return()
                            print(currency_changer)
                                
                    else:
                            print("Not a valid option.You lose!")
                elif answer == "no":
                    print("Are you sure that you can keep your golds? (yes/no?) ")
                    if answer == "yes":
                        print("You Won!")
                    elif answer == "no":
                        print("You Lost the game!")
                    else:
                        print("Not a valid option.You lose!")
                else:
                    print("Not a valid option.You lose!")

            elif answer == "no":
                print("You didn't recieved these golds anf=d lose the Game! ")
                # break
            else:
                print("Not a valid option.You lose!")

        elif answer == "no":
            print("You ignore them and offended and lose the game!")
        else:
            print("Not a valid option.You lose!")

    else:
        print("Not a valid option.You lose!")





else:
    print("Not a valid option.You lose!")



print("Thank you for trying ", name )
