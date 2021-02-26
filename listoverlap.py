import random 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

  
# using random.sample() 
# to generate random number list 
a = random.sample(range(1, 100), 10)
b = random.sample(range(1, 100), 15) 
  
# printing result 
print ("Random number list is : " +  str(a)) 
print ("Random number list is : " +  str(b)) 
for x in a:
    for y in b:
        if x == y:
            c.append(x)
c = list(dict.fromkeys(c))
print("Numbers in common:", c)
