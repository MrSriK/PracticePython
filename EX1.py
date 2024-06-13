n1=int(input("Enter a number"))
n2=int(input("Enter second number"))
print("Choose which operation to perform\n1.Addition\n2.Subtraction\n3.Division\n4.Multiplication\n5.Floor Division\n6.Exponential")
option=int(input())
match option:
    case 1:
        print("Addition is ",n1+n2)
    case 2:
        print("Subtraction is ",n1-n2)
    case 3:
        if n2!=0:
            print("Division is ",n1/n2)
        else:
            print("Invalid denominator")
    case 4:
        print("Multiplication is ",n1*n2)
    case 5:
        if n2!=0:
            print("Floor Division is ",n1//n2)
        else:
            print("Invalid denominator")     
    case 6:
        print("Exponential is ",n1**n2)   
    case _:
        print("Invalid input")