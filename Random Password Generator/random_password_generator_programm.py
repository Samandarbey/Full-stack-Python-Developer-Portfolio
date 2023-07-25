import random
import string

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long your password would you like to be? "))
    
    random.shuffle(characters)
    
    password = []
    
    for x in range(password_length):
        password.append(random.choice(characters))
        
    random.shuffle(password)
    
    password = "".join(password)
    
    print(f"This is your a new password:  {password}")
    
    
option = input("Do you wanna generate a new password? (Yes/No) ").lower()


if option == "yes":
    generate_password()
elif option == "no":
    print("Program has finished! ")
    quit()
else:
    print("Invalid value, Please enter Yes or NO: ")
    if option=="yes":
        generate_password()
    else:
        print("Finished!")
        quit()