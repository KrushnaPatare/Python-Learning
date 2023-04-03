with open("poem.txt", "r") as f:
    data=f.read()
    print(data)
    
    
if "twinkle" in data:
    print("Twinkle is present in poem.txt")
else:
    print("Twinkle is not present in poem.txt")
