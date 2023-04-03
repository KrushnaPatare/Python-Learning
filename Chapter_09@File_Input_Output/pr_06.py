

with open("log.txt", "r") as f:
    i=0
    for a in range(1,62):
        content=f.readline()
        if 'python' in content.lower():
            i+=1

print("Python = " +str(i))

