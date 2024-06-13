#Explicit Typecasting
a="10"
b=5
print(a,"+",b,'is equal to',int(a)+b) #Typecasted a from string to int for arithmetic operation
a="T"
b=20
print("The ",a,b," tournament is about to begin",sep='') #sep used to keep no space between a and b

#Implicit Typecasting
a=100.6
b=9
print(a,"-",b,"is equal to",a-b) #higher order datatype Float takes precedence over int so b is typecasted implicitly to float
c="40"
d="50"
print(c+d) #concatenation
# print(c-d) or any other arithmetic operator is useless here