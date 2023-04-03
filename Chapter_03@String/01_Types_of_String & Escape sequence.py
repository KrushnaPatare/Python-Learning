#Single quote--> ' '
#Double quote--> " "
#Triple quote--> ''' '''

# To avoid confusion of compiler
# if a string contains ' ' then use " " or ''' '''
# if a string contains " " then use ' ' or ''' '''

computer="Vishal's Computer"
sentence='''He said,"It was Great movie!"'''
print(computer)
print(sentence)

#Escape character sequence
# \--> (Single backslash) 1)\' 2)\" 3)\\ --> if you want to print 1)' 2)" 3)\ in case of 1)'' 2)"" 3)'' or ""
# \n--> (New Line) it is used to move cursor to next line
# \t--> (Tab) to give certain space in line
# ref. from above  \\--> (double backslash) to give single backslash when we are copying folder path 

# if we use '' and "" for string then we have to use \n for next line
# red='RRRRRRRRRRRRRRRRRR
#      EEEEEEEEEEEEEEEEEE
#      DDDDDDDDDDDDDDDDDD'  #this is not legal

red='RRRRRRRRRRRRRRRRRR\nEEEEEEEEEEEEEEEEEE\nDDDDDDDDDDDDDDDDDD'
print(red)
print()
red="RRRRRRRRRRRRRRRRRR\nEEEEEEEEEEEEEEEEEE\nDDDDDDDDDDDDDDDDDD"
print(red)
print()

#''' '''' --> mostly used without any condition
red='''RRRRRRRRRRRRRRRRRR
       EEEEEEEEEEEEEEEEEE
       DDDDDDDDDDDDDDDDDD'''
print(red)
