letter='''Dear <|Name|>,
We are happy to announce that you are selected.
You will work as software tester in ABC Tech.
You have to join on next months 1st date.
Date: <|Date|>.'''

Name=input("Enter your name:")
Date=input("Enter the date:")
print()
letter=letter.replace("<|Name|>",Name)
letter=letter.replace("<|Date|>",Date)
print(letter)