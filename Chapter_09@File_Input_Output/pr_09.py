import os
with open("name.txt","r") as f:
    data=f.read()
with open("renamedByPython.txt","w") as f:
    f.write(data)
os.remove("name.txt")