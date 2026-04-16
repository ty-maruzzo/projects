#functions,conditionals


import math

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero."

def square(num):
    return num ** 2

def sqrt(num):
    if num >= 0:
        return math.sqrt(num)
    else:
        return "Cannot take square root of negative number."

def binary(num):
    return bin(num)

def hexadecimal(num):
    return hex(num)

def octal(num):
    return oct(num)

print("Simple Calculator")
print("Options: add, subtract, multiply, divide, square, square root, convert (binary/hexadecimal/octal), quit")

while True:
    ask_calc = input("What do you need? ").lower().strip()
    
    if ask_calc == "quit":
        print("Goodbye!")
        break
    elif ask_calc in ["add", "subtract", "multiply", "divide"]:
        try:
            num1 = float(input("First number: "))
            num2 = float(input("Second number: "))
            if ask_calc == "add":
                answer = add(num1,num2)
                print(answer)
            elif ask_calc == "subtract":
                answer = subtract(num1,num2)
                print(answer)
            elif ask_calc == "multiply":
                answer = multiply(num1,num2)
                print(answer)
            elif ask_calc == "divide":
                answer = divide(num1,num2)
                print(answer)
        except ValueError:
            print("Invalid input. Please enter numbers.")
           
    elif ask_calc == "square":
        try:
                num = float(input("Number to square: "))
                print(square(num))
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif ask_calc == "square root":
        try:
            num = float(input("Number to find square root of: "))
            print(sqrt(num))
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif ask_calc == "convert":
        try:
            num = int(input("Number to convert (integer): "))
            ask_convert = input("To binary, hexadecimal, or octal? ").lower().strip()
            if ask_convert == "binary":
                print(binary(num))
            elif ask_convert in ["hexadecimal", "hex"]:
                print(hexadecimal(num))
            elif ask_convert == "octal":
                print(octal(num))
            else:
                print("Invalid conversion type.")
        except ValueError:
            print("Invalid input. Please enter an integer.")
    else:
        print("Invalid option. Try again.")
    break
while True:
    ask_calc = input("Do you want to keep going? Y/N ").lower().strip()
    temp = answer
    if ask_calc == "y":
        print("Options: add, subtract, multiply, divide, square, square root, convert (binary/hexadecimal/octal), quit")
        ask_calc = input("What do you need? ").lower().strip()
    if ask_calc == "n":
        break
    try:
        if ask_calc == "add":
            num = float(input("Enter Number :"))
            answer = add(temp,num)
            print(answer)
        elif ask_calc == "subtract":
            num = float(input("Enter Number :"))
            answer = subtract(temp,num)
            print(answer)
        elif ask_calc == "divide":
            num = float(input("Enter Number :"))
            answer = divide(temp,num)
            print(answer)
        elif ask_calc == "multiply":
            num = float(input("Enter Number :"))
            answer = multiply(temp,num)
            print(answer)
        elif ask_calc == "convert":
            temp = int(answer)
            ask_convert = input("To binary, hexadecimal, or octal? ").lower().strip()
            try :
                if ask_convert == "binary":
                    answer_binary = binary(temp)
                    print(answer_binary)
                elif ask_convert in ["hexadecimal", "hex"]:
                    answer_hex = hexadecimal(temp)
                    print(answer_hex)
                elif ask_convert == "octal":
                    answer_octal = octal(temp)
                    print(answer_octal)
                else:
                    print("Invalid conversion type.")
            except ValueError:
                print("Please Enter Valid Input")
        elif ask_calc == "square":
            answer = square(temp)
            print(answer)
        elif ask_calc == "square root":
            answer = sqrt(temp)
            print(answer)
    except ValueError:
        print("Invalid input. Please enter an integer.")
    
