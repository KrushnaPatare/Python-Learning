num=int(input("Enter the number:"))
l=[]
for i in range(1,11):
 #   a=str(num)+"*"+str(i)+"="+str(num*i)
    a=f"{num} * {i} = {num*i}"
    l.append(a)
l.reverse()
print(l)

for i in reversed(range(1,11)):
    print(str(num)+"*"+str(i)+"="+str(num*i))
    #print(f"{num} * {i} = {num*i}") #f string