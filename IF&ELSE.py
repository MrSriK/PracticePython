#Conditional Operators <,>,==,!=,<=,>=
num=int(input("Enter a number: "))
if(num>0):
    if(num<10):
        print("number is single digit positive")
    elif(num<100):
        print("Number is double digit positive")
    else:
        print("Number is some-digit positive integer")
elif(num<0):
    if(num>-10):
        print("number is single digit negative")
    elif(num>-100):
        print("Number is double digit negative")
    else:
        print("Number is some-digit negative integer")
else:
    print("Number is Zero")