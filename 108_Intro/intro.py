
from dataclasses import asdict
from turtle import addshape


print("Hello world from Python!!")

name = "hai"
last_name = "nguyen"
print(name, last_name)
age = 99
total = 23.123
found = False
# comments....
print(age, total, found)

if (age < 100):
    print("don't worry")
    print("don't worry")
    print("don't worry")
elif (age == 100):
    print("congrat")
    print("congrat")
    print("congrat")
else:
    print("sorry")

print("outside")

# math operator
2+3
3*4

# functions


def say_hello():
    print("hello there")
    print("i'm inside the function")


say_hello()
say_hello()
