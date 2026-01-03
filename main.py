import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return math.pow(x, y)

def square_root(x):
    return math.sqrt(x)

def logarithm(x):
    return math.log(x)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))


print("==== SCIENTIFIC CALCULATOR ====")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power (x^y)")
print("6. Square Root")
print("7. Logarithm")
print("8. Sine")
print("9. Cosine")
print("10. Tangent")

while True:
    choice = input("\nEnter choice (1-10) or 'q' to quit: ")

    if choice.lower() == 'q':
        print("Exiting Calculator. Goodbye!")
        break

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        elif choice == '5':
            print("Result:", power(num1, num2))

    elif choice in ('6', '7', '8', '9', '10'):
        num = float(input("Enter number (in degrees for trig functions): "))

        if choice == '6':
            print("Result:", square_root(num))
        elif choice == '7':
            print("Result:", logarithm(num))
        elif choice == '8':
            print("Result:", sine(num))
        elif choice == '9':
            print("Result:", cosine(num))
        elif choice == '10':
            print("Result:", tangent(num))

    else:
        print("Invalid input. Please try again.")
