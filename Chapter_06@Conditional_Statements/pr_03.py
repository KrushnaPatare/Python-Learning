comment=input("Enter the text \n")
spam=False

if("make a lot of money" in comment):
    spam=True
elif("buy now" in comment):
    spam=True
elif("subscribe this" in comment):
    spam=True
elif("click on this" in comment):
    spam=True
else:
    spam=False

if(spam):
    print("This text is spam.")
else:
    print("This text not is spam.")
