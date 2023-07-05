def email_slicer():
    print("Welcome to the Email Slicer!  ")
    print("")
    
    email_receiver = input("Enter your email address, please: \n")
    
    (username, domain) = email_receiver.split("@")
    (domain, extension) = domain.split(".")
    
    print("Username : ", username)
    print("Domain : ", domain)
    print("Extension:",extension)
    
while True:
    email_slicer()