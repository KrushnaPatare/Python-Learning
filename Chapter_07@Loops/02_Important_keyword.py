#break keyword
for e in range(0,11):
    print(e)
    if (e==5):
        break   
else:
    print("This will not print.")
print()


#continue keyword
for f in range(20,26):
    
    if (f==22):
        continue
    print(f)
else:
    print("ABC")


#pass keyword    --> if we don't wont to write code in condition or loop
#                   without pass programme will throw error.
for f in range(20,26):
    pass
else:
    pass



for f in range(20,26):
    
    if (f==22):
        pass

#reversed keyword
for i in reversed(range(1,11)):
    print(str(num)+"*"+str(i)+"="+str(num*i))
    #print(f"{num} * {i} = {num*i}") #f string