#recursion - the function that calls itself is called recursive function.

def rec(n):
    if n==1 or n==0:
        return 1
    else:
        return n*rec(n-1)

print(rec(5))
       #5*rec(4)
       #5*4*(rec(3)
       #5*4*3*(rec(2)
       #5*4*3*2*rec(1)
       #5*4*3*2*(1)  #rec(1)=1

#Tip: coder has to make sure that programme doesn't go in infinite recursion.