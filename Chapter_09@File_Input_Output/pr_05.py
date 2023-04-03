words=["black","bad","crime","drugs"]

with open("news.txt","r") as f:
    data=f.read()

print(data)
print()

for word in words:
    data=data.replace(word,"######")

with open("news.txt","w") as f:
    f.write(data)

print(data)