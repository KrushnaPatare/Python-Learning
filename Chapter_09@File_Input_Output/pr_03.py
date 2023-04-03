for i in range(2,6):
    with open("Table of "+str(i)+".txt", "w") as f:
        for a in range(1,11):
            f.write(f"{i} * {a} = {i*a}\n")
    