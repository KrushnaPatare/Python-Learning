#while loop --> will work until condition is true.

fruits=["Mangos","Grapes","Blueberry","Papaya","Apple"]
i=0
while i<len(fruits):
    print(fruits[i])
    i=i+1
print()

#for loop - will work until fixed iterations are complited.

for item in fruits:     #here, item is a keyword you can not use other word instead of 'item'.
    print(item)
print()


#range function 

for i in range(10): #starts from 0 to n-1    (0 to 9)
    print(i)
print()

for a in range(5,16): #starts from 5 to n-1    (5 to 15)
    print(a)
print()

for c in range(10,51,5): #starts from 5 to n-1    (5 to 15)
    print(c)
print()



#for-else loop
for d in range(0,16):
    print(d)
else:
    print("This is else of for loop.")
print()


for a in range(5,4): #starts from 5 to n-1    (5 to 15)
    print(a)
print()

num=3
prime=True
for i in range(3,num):
    if num%i==0:
        prime= False
        break
print(prime)
