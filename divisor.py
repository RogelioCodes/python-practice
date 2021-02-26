num = int(input("Enter a number: "))
listRange = list(range(1,num+1))

divisorlist = []
for elem in listRange:
    if num % elem == 0:
        divisorlist.append(elem)
print(divisorlist)



