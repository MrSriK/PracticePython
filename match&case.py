x=int(input("Enter a number: "))
match x:
    case 0:
        print(x,"is neither positive, nor negative")
    case 1:
        print(x,"is the smallest positive integer")
    case -1:
        print(x,"is the largest negative integer")
    case _ if(x%2==0 and x<0):
        print(x,"is a negative even number")
    case _ if(x%2==0 and x>0):
        print(x,"is a positive even number")
    case _:
        print(x,"is an integer")
#we can have more than one default statement