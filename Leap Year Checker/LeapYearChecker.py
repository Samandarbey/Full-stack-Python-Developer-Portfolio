import random

print("Welcome to this program that helps you to analyse does this year  'Leap Year' or Not!  ")
while True:
    year = int(input("Enter your wanted year to this program: \n"))

    def is_leap_year(year):
        if year % 4 == 0:
            if year % 1 == 0:
                if year % 400 == 0:
                    print(f"{year} is Leap Year!")
                else:
                    print(f"{year} is Not Leap Year")
            else:
                print(f"{year} is Leap Year")
        else:
            print(f" {year} is Not Leap Year")
            
    is_leap_year(year)
        
        
# while True:
#     ask = input("Are you ready? (yes/no)").lower()
#     if ask == "yes":
#         is_leap_year(year)
#     elif ask == "not":
#         print("Think again!")
#         quit()
#     else:
#         print("Invalid Option, choose yes/no! ")
    




# is_leap_year(2022)