list=["Harry","Ram","Sham"]

for i in range(0,3):
    name=list[i]

    def remove_and_strip(str,word,name):
        new_str = str.replace(word,name)
        return new_str.strip()
    sentence="     Tom is a good boy.   "
    print(sentence)
    print(remove_and_strip(sentence,"Tom",name,))





