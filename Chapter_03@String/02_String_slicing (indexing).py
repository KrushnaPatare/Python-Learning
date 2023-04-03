name="Krushna"
#     0123456  --> index numbers of characters in string
surname="Patare"
fullName=name+surname   # concatenating (attaching) of two string
print(fullName)
print(fullName[3])   # printing single character from string
print(fullName[5])  
print(fullName[7])  
print(fullName[2:7]) # will print 2,3,4,5,6 index characters (range)
print(fullName[4:])   # same as [4:13] ,by default upto last character from given index number
print(fullName[:9])   # same as [0:9] , by default upto given character from first index number that is 0
print(fullName[::3])  # it will print each third chracter in given string sequence.
print()

# Negative Indexing
#index of characters can be negative for different purpose we can use them.
name="Krushna"
#    -7-6-5-4-3-2-1
# print(name[-1:-4]) this is wrong because here index is starting from last number
print(name[-4:-1])
print(name[:-1])
print(name[-7:])
print(name[-6:-1:2])  #print each second letter in given string range
