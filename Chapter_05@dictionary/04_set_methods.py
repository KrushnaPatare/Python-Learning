#Set Methods
s={1,2,'A',99.99,"fun",True}

#add() --> adds values in set
s.add("Beauty")
s.add(525)
#s.add([1,2,3]) cannot add list in set because it is mutable
s.add((1,2,3)) #tuple can be added in set
#s.add({"day:sunday"}) cannot add dictionary in set because it is mutable
print(s)
print()

#len() --> returns length of set
print(len(s))
print()

#remove() --> removes given value 
s.remove(99.99)
print(s)
print()

#pop() --> remove the random value and retuens that value
print(s.pop())
print(s)
print()

#clear() --> deletes the all values in set and return None(null) or empty set
ss={1,2,3,4,5}
print(ss)
print(ss.clear()) #returns None(null)
print(ss) # returns empty set
print()

#union() --> returns combination of two sets
set={1,2,3,4,5}
sett={10,20,30}
print(set)
print(sett)
print(set.union(sett))
print(set.union({16,25,36,49,64}))
print()

#intersection()  --> returns the common values
a={1,2,3,4,5,6,7,8,9}
b={2,4,6,8,10,12}
print(a)
print(b)
print(a.intersection(b))
print(a.intersection({4,8,10}))
print()

#Learnings
#set is unordered.
#set is unindexed -- cannot access by index.
#values in set are unchangable.
#set cannot contain duplicate values.

