import math

def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def power(x, y):
    return math.pow(x,y)
def mod(x,y):
    return x % y
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

print("==============================================")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Modulo")
print("7. Exit")
print("==============================================")
choice = True 
while choice:
    choice = input("Please select the calcultion option: ")
    if choice == '1':
        print(num1,"+",num2,"=", add(num1,num2))
        break
    elif choice == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))
        break
    elif choice == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))
        break
    elif choice == '4':
        print(num1,"/",num2,"=", divide(num1,num2))
        break
    elif choice == '5':
        print(num1, "to the power of", num2, "is", power(num1,num2))
        break
    elif choice == '6':
        print(num1, "%", num2, "=", mod(num1,num2))
        break
    elif choice == '7':
        print("\nClosing calculator. Thanks for using.")
        raise SystemExit
    elif choice != "":
        print("\nInvalid input")
       