with open("badword.txt", "r") as f:
    data=f.read()
print(data)

data=data.replace("Donkey", "Elephant")

with open("badword.txt", "w") as f:
    f.write(data)

print(data)