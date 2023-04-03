l=["Harry","Soham","Sachin","Rahul"]
for item in l:
    w=item[0]
    if w=="S":
        print("Welcome",item)
print()

for item in l:
    if(item.startswith("S")):
        print("Welcome "+item)