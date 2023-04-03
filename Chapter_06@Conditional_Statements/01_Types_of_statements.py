#if statement
a=99
if(a>100):
    print("A is greater than 100.")
    print("End")

print()

b=110
if(b>100):
    print("B is greater than 100.")

    print("Gap doesn't matter.")

print("End")

print()

#if code has an indentation then it is in border of if statement.
# and gap between lines doesn't matter as long as indentation is there.

#if-else statement
if(a<b):
    print("A is smaller than B.")
else:
    print("A is greater than B.")
print()

#if-elif-else statement
c=110
if(a>b):
    print("A is greater than B.")
elif(a>=b):
     print("A is smaller than B.")
elif(c==b):
    print("C is equal to B.")
else:
    print("A,B,C are different.")
print()

#optional else
if(a>b):
    print("A is greater than B.")
elif(a>=b):
     print("A is smaller than B.")
elif(c==b):
    print("C is equal to B.")
print()
# else: #here else statement can be optional.
#     print("A,B,C are different.")

#nested if statement
day="sunday"
wakeUp=8
money=True
tea=True

if(day=="sunday"):
    print("Today is holiday.")
    if(wakeUp>=5 and wakeUp<=7):
        print("Go to morning walk.")
        if(money==True):
            print("Buy milk pouch.")
            if(tea==True):
                print("Make tea, drink it & relax.")
            else:
                print("Drink water.")
        else:
            print("Don't buy anything.")
    else:
        print("Stay home, watch Netflix.")
else:
    print("Working day - go to office.")

