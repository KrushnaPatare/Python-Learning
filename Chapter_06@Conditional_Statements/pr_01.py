num1  = int(input("Enter number 1:"))
num2  = int(input("Enter number 2:"))
num3  = int(input("Enter number 3:"))
num4  = int(input("Enter number 4:"))
'''
if(num1>num2 and num1>num3 and num1>num4):
    print("The greatest number =",num1)
elif(num2>num1 and num2>num3 and num2>num4):
    print("The greatest number =",num2)
elif(num3>num1 and num3>num2 and num3>num4):
    print("The greatest number =",num3)
elif(num4>num1 and num4>num2 and num4>num3):
    print("The greatest number =",num4)
else:
    print("Nobody is greater because two numbers are equal.")
print()'''


#without using Logical operaor
#(for this example each number should be differnt strictly.)
if(num1>num2):
    n1=num1
else:
    n1=num2

if(num3>num4):
    n2=num3
else:
    n2=num4

if(n1>n2):
    print("The greatest number is "+str(n1))
else:
   print("The greatest number is "+str(n2))
