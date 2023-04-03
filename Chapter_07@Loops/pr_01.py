num=int(input("Enter the number to get its table:"))

for i in range(0,11):
    print(str(num)+"*"+str(i)+"="+str(num*i))
    print(f"{num} * {i} = {num*i}") #f string