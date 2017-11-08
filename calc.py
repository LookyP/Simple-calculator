import math
import sys
import time
def main():
    process = input("Input the process you would like to complete. multiply, divide, add, subtract, root, raise to power: ")
    if process == "add":
        add()
    elif process == "subtract":
        subtract()
    elif process == "multiply":
        multiply()
    elif process == "divide":
        divide()
    elif process == "root":
        root()
    elif process == "raise to power":
        power()
    else:
        print("invalid input. type one of the options")
        main()
def add():
    try:
        firstNum = float(input("Input the first number for addition: "))
        secondNum = float(input("Input the second number for addition: "))
        total = secondNum + firstNum
        print(total)
        
    except:
        print("Invalid input. Try again")
        add()
    again()
def subtract():
    try:
        firstNum = float(input("Input the first number for subtraction: "))
        secondNum = float(input("Input the second number for subtraction: "))
        total = firstNum - secondNum
        print(total)
        
    except:
        print("Invalid input. Try again")
        subtract()
    again()
def multiply():
    try:
        firstNum = float(input("Input the first number for multiplication: "))
        secondNum = float(input("Input the second number for multiplication: "))
        total = firstNum * secondNum
        print(total)
        
    except:
        print("Invalid input. Try again")
        multiply()
    again()
def divide():
    try:
        firstNum = float(input("Input the first number for division:"))
        secondNum = float(input("Input the second number for division: "))
        total = firstNum / secondNum
        print(total)
        
    except:
        print("Invalid input. Try again")
        divide()
    again()
def root():
    try:
        rootval = float(input("input a root. For example, 2 for square root, 3 for cube root, etc: "))
        num = float(input("input the number you want to root: "))
        total = math.pow(num,1/rootval)
        print(total)
        
    except:
        print("Invalid input. Try again")
        root()
    again()
def power():
    try:
        num = float(input("Input a number you that you want to raise to a power: "))
        index = float(input("Input the power you want to raise it by: "))
        total = math.pow(num,index)
        print(total)
        
    except:
        print("Invalid input. Try again")
        power()
    again()
def again():
    dec = input("Again?: ")
    if dec == 'yes':
        main()
    elif dec == 'no':
        print("Exiting in three seconds")
        time.sleep(3)
        sys.exit()
    else:
        print("invalid input. Type yes or no")
        again()


    
main()
