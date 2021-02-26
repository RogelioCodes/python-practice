num = int(input("Enter a number: "))
if num % 2 == 0:
    if num % 4 == 0:
        print("Number is even and a multiple of four")
    else: 
        print ("Number is even")
else: 
    print("Number is odd")

num = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

if num % num2 == 0:
    print(num, "divides evenly by", num2)
else:
    print (num, "doesnt divide evenly by", num2)