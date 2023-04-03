story="Once there was farmer who grew Mango tree."

#len() --> gives the length of string
print("len()")
print(len(story))

#endswith() --> gives True or Faldse result
print("endswith()")
print(story.endswith("tree."))

#count() --> tells a charater or set of characters how many times are there in string
print("count()")
print(story.count("e"))
print(story.count("re"))

#capitalise() --> makes first letter of string or a character capital.
l="little"
h='k'
print("capitalise()")
print(l.capitalize())
print(h.capitalize())

#find() --> tells, index of character of first character at first occurance in given string of given set of characters.
print("find()")
print(story.find("was"))
print(story.find("c"))

#replae() --> replaces word in a string
print("replae()")
story=story.replace("farmer", "doctor")
print(story.replace("tree","juice"))

