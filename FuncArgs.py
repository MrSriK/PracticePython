'''
Types of args that can be passed to a function
->Default
->Required
->Keyword
->Variable Length
'''

#default args
def Addition(a=10,b=20):
    print("Inside Addition, Values are: a =",a,"and b =",b)
    print(a,"+",b,"=",a+b)
Addition()  #will take default value of a and b
Addition(33)    #Sets a to 33 and takes default value of b
Addition(b=56)  #Sets b to 56 and takes default value of a
Addition(4,5)   #Sets both a and b to passed values

#keyword
def DisplayName(first,middle,last="Junior"):
    print("Hello",first,middle,last)

DisplayName(middle="Sainz",first="Carlos") #This will work as we have specified the keyword values
DisplayName(last="Senior",first="Carlos",middle="Sainz")

#required
def isGreater(a,b=100): #Here, a is the required argument, without which the function will not work
    if(a>b):
        print(a,">",b)
    else:
        print(b,'>',a)
isGreater(10)

#variable length---Tuple
def average(*numbers):  #We can pass multiple arguments, they get passed as a tuple which is immutable
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is",sum/len(numbers))
average(5,6)
average(1,2,3)
average(4,5,2,4,677,1334)

#variable length---Dictionary
def DispName(**name):   #Arguments are passed as Ke-Value pairs or Dictionary
    print("Inside DispName Variable Length Function")
    print('Hello',name['fname'],name['mname'],name['lname']) #Printing name.fname, name.mname,name.lname
DispName(lname='Jones',mname='Bones',fname='Jon')   #Stored as name={lname:'Jones',mname:'Bones',fname:'Jon'}

#The return keyword returns a value from the called function that can be stored in a variable
def isEven(num):
    if(num%2==0):
        return True
    else:
        return False
x=int(input("Enter a number to check if it is Even or not: "))
checker=isEven(x)
print('It is',checker,'that',x,'is Even')


