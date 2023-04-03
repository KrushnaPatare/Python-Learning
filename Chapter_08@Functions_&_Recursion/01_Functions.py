#Function Types:

#1]Buit in function:
print()       #this is defalut or built in function

#2]User defined function:
def mySum(num1,num2):
    h=num1+num2
    return h

k=mySum(10,20)
print(k)

def greet(name):
    return "Hello "+name

a=greet("Sham")
print(a)


#Defalut value
def mobnum(num=100): #num=100 is defalut variable value when we dont enter any.
    return "Default mobile number to call police is "+str(num)

n=mobnum()
print(n)