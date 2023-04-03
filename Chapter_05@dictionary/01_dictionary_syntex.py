#Dictionary stores data in terms of key:value

dictionary={
    #Key : Value
    "ok" : "All Correct",
    "MRI" : "Magnetic Resonance Imaging",
    "Marks" : [85,86,89,87,90]
}

print(dictionary["ok"])
print(dictionary["MRI"])
print(dictionary["Marks"][2]) #giving index of value to related  key for print
print()

#Nested Dictionary

dictionary01={
    "ok" : "All Correct",
    "MRI" : "Magnetic Resonance Imaging",
    "Marks" : [85,86,89,87,90],
    "newdir" : { "day1" : "sunday",
                 "day2" : "monday",
                      5 : 25      }
}

print(dictionary01["newdir"])
print(dictionary01["newdir"]["day1"])
print()

#Add values with new key names

dictionary01["mobile"] = "9860187937"
dictionary01["school"] = "Residential High School"
print(dictionary01)
