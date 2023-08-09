# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
print("Welcome to our PyCharm python program! \n")
print("We are gonna calculte the quadratic form of your input number, bro!")


def main():
    number = int(input("Enter your number to execute the sequence of it... \n"))
    answer = number ** 2

    # return answer
    print(f"Answer is {answer}")

matter = 0
while True:
    ask = input("Are you ready? (yes/no) \n").lower()
    if ask == "yes":
        print("Let's get started! \n")
        main()
        matter += 1
        if matter >=2:
            print(f"Your tryings are {matter}")
        else:
            print(f"Your trying is {matter}")

    elif ask == "no":
        print("Good Bye, Fuck of yourself! \n")
        print(f"You tried {matter} times, thanks!")
        quit()
    else:
        print("Invalid option bro, type yes or no !")
        continue

