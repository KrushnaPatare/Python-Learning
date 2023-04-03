sub1 = int(input("Enter the marks os sub1 ="))
sub2 = int(input("Enter the marks os sub2 ="))
sub3 = int(input("Enter the marks os sub3 ="))


percent=(sub1+sub2+sub3)/300*100
print(percent)

if(sub1<33 or sub2<33 or sub3<33 or percent<40):
    print("Student is failed.")
else:
    print("Student is passed.")