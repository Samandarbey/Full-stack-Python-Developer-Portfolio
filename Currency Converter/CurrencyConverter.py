# import lambda as lam 
print("Welcome to the program that can help you to convert your US dollars to Pounds Sterling and Pounds Sterlings to US dollars. ")


def first():
    print("This program converts US dollars to Pounds Sterling")
    print()
    
    dollars = eval(input("Enter the amount in dollars: "))
    
    pounds = convert_to_pounds(dollars)
    
    print("That is", pounds, "pounds.")
    
convert_to_pounds = lambda dollars: dollars * 0.82


def second():
    print("This program converts  Pounds Sterling to US dollars ")
    print()
    
    pounds = eval(input("Enter the amount in Pounds Sterling: "))
    
    dollars = convert_to_pounds(pounds)
    
    print("That is", dollars, "dollars.")
    
convert_to_pounds = lambda pounds: pounds * 1.18


while True:
    ask = input("Choose one of these two options: \n First:  US $ to Pounds Sterling & \n Second: Pounds Sterling & to US $ ").lower()
    if ask == "first":
        first()
    elif ask == "second":
        second()
    else:
        print("Invalid option! Change it please!")
        




