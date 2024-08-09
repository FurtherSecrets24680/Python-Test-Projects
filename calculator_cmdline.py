# Modules
import math
import os
import shutil

# Intro
print("Welcome to CLICALC v1.0! A very easy to use command line calculator written in Python!")

# Input
first = float(input("First number: "))
second = float(input("Second number: "))
operator = input("Select an operator: ")

# Operators
if operator == "+":   # Addition
    print(first + second)
elif operator == "-": # Subtraction
    print(first - second)
elif operator == "*": # Multiplication
    print(first * second)
elif operator == "/": # Division
    print(first / second)
    
# Functions   
elif operator == "sqrt": # Square Root
    print("The square root of " + str(first) + " is " + str(math.sqrt(first)))
elif operator == "pow":  # Power / Exponent / Index
    print(pow(first, second))
elif operator == "fact": # Factorial
    print((math.factorial(int(first))))
elif operator == "abs":  # Absolute Value
    print(abs(int(first)))

# Easter Eggs
elif operator == "rickroll":
    os.system("curl ascii.live/rick")
    
elif operator == "wincalc":
    os.system("calc.exe")
    
#Errors
else:
    print("Invalid Operator")

    
