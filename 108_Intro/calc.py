

# function
import re


def print_menu():
    print("***PyCalc***")
    print("--------------")
    print("[1] sum")
    print("[2] subtract")
    print("[3] Multiply")
    print("[4] Devision")


def sum(num1, num2):
    result = num1+num2
    print("the result is: " + str(result))


def sub(num1, num2):
    result = num1-num2
    print("the result is: " + str(result))


def mul(num1, num2):
    result = num1*num2
    print("the result is: " + str(result))


def dev(num1, num2):
    if num2 == 0:
        print("Error: 0 is not allow")
    else:
        result = num1/num2
        print("the result is: " + str(result))


# plain instruction
opt = ""
while opt != "q":
    print_menu()

    opt = input("please input option..:")
    if opt == "q":
        break

    num1 = float(input("input number 1: "))
    num2 = float(input("input number 2: "))
    if opt == "1":
        sum(num1, num2)
    elif opt == "2":
        sub(num1, num2)
    elif opt == "3":
        mul(num1, num2)
    elif opt == "4":
        dev(num1, num2)

    print("")
    input("Press Enter to Conitue...")
    print("\n\n\n")
