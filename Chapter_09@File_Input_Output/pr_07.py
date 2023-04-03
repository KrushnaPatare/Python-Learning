with open("abc.txt", "r") as f:
    data=f.read()

with open("abc2.txt", "w") as f:
    f.write(data)

with open("abc2.txt", "r") as f:
    data2=f.read()

if data==data2:
    print("abc.txt and abc2.txt file are identical.")
else:
    print("abc.txt and abc2.txt file are not identical.")

