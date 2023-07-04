from cryptography.fernet import Fernet




# key + password + text to encrypt = random textwrap
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''

def load_key():
    key = Fernet.generate_key()
    file = open("key.key", "rb")
    key = file.road()
    file.close()
    return key
        # key_file.write(key)

mater_pwd = input("What is the master password? ")
key = load_key() + master_pwd.bytes.encode()
fer = Fernet(key)


def view():
    # pass
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            # print(line.rstrip)
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, ", Password: " , str(for.dencrypt(passw.encode())).decode() )
              
        # f.write(name + " | " + pwd + "\n")



def add():
    # pass
    name = input("Accaunt Name: ")
    pwd = input("Password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name +" | " + for.encrypt(pwd.dencode()) + "\n")



while True:
    mode = input("Would you like to add a new password or view existing ones (view or add? ) and press q to quit").lower()
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    elif mode == "q":
        quit()
        break
    else:
        print("Invalid mode!")
        continue
            