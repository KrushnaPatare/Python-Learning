s=set()
s.add(20)
s.add("20")
s.add(20.0)
print(s) # it will hold only two values 20 & "20", because 20 is equal 20.0
print(len(s)) #it will show length= 2
print()


ss=set()
ss.add(50)
ss.add("50")
ss.add(50.5)
print(ss)
print(len(ss))