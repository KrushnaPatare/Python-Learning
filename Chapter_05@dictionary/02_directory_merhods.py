dictionary={
    "ok" : "All Correct",
    "MRI" : "Magnetic Resonance Imaging",
    "Marks" : [85,86,89,87,90],
    "newdir" : { "day1" : "sunday",
                 "day2" : "monday",
                      5 : 25      }
}

#keys() --> returns all keys
print(dictionary.keys()) # shows the all keys present in dictionary.
totalKey = list(dictionary.keys()) # typecasting all the result of keys() is converted in list
print(totalKey)
print()

#values() --> returns all values
print(dictionary.values())
print()

#items() --> returns all key-value pairs
print(dictionary.items())
print()

#update() -->
new={         6:36,
        "name" : "krushna",
          "ok" : "All Right" }

dictionary.update(new)
print(dictionary)
print()

#get() --> gets the value of a single given key
print(dictionary.get("ok"))
print()

#differnce between get() and []
print(dictionary.get("Good")) #will show None, if key is not present
'''print(dictionary["Good"])''' #will throw errror, if key is not present so this depends upon user
                          #user has to know correct key

#Learing
#dictionary is unordered --> we cannot call item by index number.
#dictionary is mutable.
#dictionary is indexed --> order of key:value once created cannot be changed it will print according to keys sequence.
#dictionary cannot contain duplicate keys.