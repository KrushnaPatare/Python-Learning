a=[1,25,7,3,15,12]

# 1)sort() --> sort in ascending order
# as=a.sort() -- this is wrong here because sort() method is not returning result,
#it is actually making change in (a) directly.
a.sort()
print(a)
print()

# 2)reverse() --> will reverse values (no descending order - try on unorganised values)
a.reverse()
print(a)
print()

# 3) append() --> adds values in list at the end
a.append(10)
print(a)
print()

# 4) insert() --> insert(add) a value in list at perticular index
a.insert(0,100)
print(a)
a.insert(3,36)
print(a)
print()

# 5) pop() --> to delete value at perticular index in list
a.pop(0)
print(a)

# 6)remove() --> to remove(delete) given value in method argument that is present in list
a.remove(36)
print(a)
print()

#clear()
#count()
#copy()
