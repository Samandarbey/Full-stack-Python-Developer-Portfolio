# define the functions needed: add, sub, mul, div
# print options to users
# ask for value
# call the functions
# while loo[ to continuie/]



def add(a,b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer))
    # print(a,b)


def sub(a,b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))
    # print(a,b)



def mul(a,b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))



def div(a,b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))


# def inputs():

    # return

print("A/a -> Addition")
print("B/b -> Subtraction")
print("C/c -> Multiplication")
print("D/d -> Division")
print("E/e -> Exit")
while True:
    choice = input("Enter your choice: \n")
    if choice == "a" or choice == "A" :
        print("Addition ")
        a =int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        # inputs()
        add(a,b)
        # break
    elif choice == "B" or choice == "b":
        print("Subtraction")
        # input()
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        sub(a,b)
        # break
    elif choice == "c" or choice=="C":
        print("Multiplication: ")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        # inputs()
        mul(a,b)
        # break
    elif choice == "D" or choice == "d":
        print("Devision: ")
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))

        # inputs()
        div(a,b)
        # break
    else:
        print("Programm has finished, Thanks!")
        quit()
        # break









