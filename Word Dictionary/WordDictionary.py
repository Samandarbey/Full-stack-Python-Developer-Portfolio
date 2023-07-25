print("Welcome to our program that helps you to find your researched words in English!")
ask = input("Are you ready? (Yes/No) \n").lower()

def main():
    word_dictionary = {
        'hi': 'a way of greeting',
        'eye':' an organ for seeing',
        'earth':'a planet in the space'
    }
    while True:
        word = input("Enter a word: \n")
        if word == " ":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])
        else:
            print("we don't have this word in our dictionary, sorry!")
            

while True:
    if ask == "yes":
        print("OK")
        main()
    elif ask == "no":
        print("Restart this program when you are ready, OK?")
        ask2 = input("Shall we start again? (yes/no) \n").lower()
        if ask2 == "yes":
            # continue
            main()
        elif ask2 == "no":
            quit()
        else:
            print("Invalid option, choose once more time! ")
    else:
            print("Invalid option, choose once more time! ")

