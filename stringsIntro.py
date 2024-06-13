s1='hello'
print(s1)
#multiline strings
print("how are you?\nhope everything good")
s2='''This is another way to
Write multiline strings and store them
Inside a variable
If not assigned to variable
This will become a 
Multiline Comment'''
print(s2)
#quoting in strings
print("The quotes 'can be applied' like this")
print("Or also \"they can be applied\" like this")
#A string is an array of characters so we can print like this also
print(s1[0])#this will give 'h' from hello
print("method 2\n")
#we can iterate through the variable one by one using a for loop, but we need not always define a length for iterator as we do in other languages
for character in s1:
    print(character)
print("now printing a multiline string\n")
for character in s2:
    print(character)