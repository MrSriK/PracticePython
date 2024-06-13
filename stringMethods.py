s1="Array"
print(s1)
#strings are Immutable so when we apply any method as follows, it is a new object, not the same
print(s1.upper())#to capitalize all characters
print(s1.lower())#to make all characters small

s2="Hello!!!!"
print(s2.rstrip("!")) #Removes a trailing set of mentioned characters from string

s3="????Hello???"
print(s3.rstrip("?")) #But does not remove leading set of mentioned characters
'''
STRINGS are IMMUTABLE
Each print statement where string method is applied, a new opject is created, no change is made to existing object
'''
s4="Python,JavaScript,Java,JavaDataBase"
#To replace a String we do this
print(s4.replace("Java","Python")) #Creates new Object, original is not affected
# To convert string to a list, do this and specify a separator
print(s4.split(","))#the comma is set as separator and hence separates each element to a different Index

s5="hinT, to Capitalize oNly first alpHabet, DO this"
print(s5.capitalize()) #It also fixes any mistakes, like a wrong character being capitalized, gets lower cased

s6="Welcome to the Console!!!"
print(len(s6)) #Returns length of s6 which is 25
print(s6.center(50))#Center given string, but the number shuould be greater than string length, However...
print(len(s6.center(50))) #The number of spaces will be 50-len(s6), so '50' specifies the total length of the string including len(s6)

#to print number of occurences in a string,
print(s4.count("Java"))
print(s6.endswith("!!!"))#returns true if string ends with '!!!'
print(s6.startswith("Welcome"))#returns true if string starts with 'Welcome'

s7="Python is an interpreted programming language, which is used widely for Data Analysis"
print(s7.find("is"))#returns the index of first occurrence of "is", will return index of i from is
print(s7.find('where')) #returns -1 if not found in string
#But if you want to raise an exception for string not being found then use index()
'''print(s7.index('where'))'''

s8="Mumbai400001"
print(s8.isalnum()) #returns true if string has A-Z,a-z or 0-9 and false if any symbols like -,+/ or Space
s8="MumbaiCentral"
print(s8.isalpha())#true if only Alphabets present
s8="400001"
print(s8.isnumeric())#true if only Numbers present
s8="hello"
print(s8.islower()) #true if all characters are lower case
print(s8.isupper()) #true if all characters are upper case
s8="Is this printable?\n"
print(s8.isprintable())#True if printable, false if we use Escape sequence Characters
s8=" "
print(s8.isspace())#True if string has only white spaces, does not matter whether Tab or Spacebar
s8="Welcome to Linux"
print(s8.istitle())#true if each word's first alphabet is capital, else false
print(s8.swapcase()) #Converts lowercase to uppercase and vice-versa
s8="Remember this Day and Age"
print(s8.title()) #converts all words' starting alphabets to uppercase