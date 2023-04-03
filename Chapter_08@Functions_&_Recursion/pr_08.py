import random

compnum = random.randint(1,3)
print("Computer Turn: Rock, Paper, Scissor.")
you = input("Your turn: Rock, Paper, Scissor: ")

if (compnum==1):
    comp="Rock"
elif(compnum==2):
    comp="Paper"
else:
    comp="Scissor"

def game(comp,you):
    if(comp=="Rock"):
        if(you=="Paper"):
            return True
        elif(you=="Scissor"):
            return False
        else:
            return None
    elif(comp=="Paper"):
        if(you=="Scissor"):
            return True
        elif(you=="Rock"):
            return False
        else:
            return None
    else:
        if(you=="Rock"):
            return True
        elif(you=="Paper"):
            return False
        else:
            return None

result=game(comp,you)

print("Computer choose "+comp)
print("You choose "+you)

if(result==True):
    print("You won!")
elif(result==False):
    print("You loose!")
else:
    print("The game is a tie!")