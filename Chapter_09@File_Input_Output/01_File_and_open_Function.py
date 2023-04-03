#There are two types of files:
#1]Text file (.txt file etc.)
#2]Binary file (.jpg, .dat file etc.)

#open function

f=open("name.txt","r")
data=f.read()  #to read all data
print(data)
f.close()  #don't forget to close file

#Types of modes: "r", "W", "a", "t"

f=open("abc.txt","r")
data=f.readline() #first line
print(data)
data=f.readline() #second line
print(data)
data=f.readline() #third line
print(data)
f.close()  #don't forget to close file

f=open("xyz.txt", "w")
f.write("I write in this file.\n")
f.write("I write in this file.\n")
f.write("I write in this file.\n")
f.write("I write in this file.\n")
f.write("I write in this file.\n")
f.close()


#with statement ----> when you use with statement    

with open("new.txt", "w") as f:
    a=f.write("Happy new year!")

print(a)


