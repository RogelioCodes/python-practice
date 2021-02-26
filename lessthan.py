a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a2 = [ num for num in a if num < 5]
print(a2)

input = int(input("Enter a number and I will insert numbers smaller than it into a list: "))
a3 = [ num for num in a if num < input]
print(a3)