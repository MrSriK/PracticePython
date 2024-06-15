def AddFunc(a,b):
    print("Addition is",a+b)
def SubFunc(a,b):
    print("Subtraction is",a-b)
def MulFunc(a,b):
    print("Multiplication is",a*b)
def DivFunc(a,b):
    print("Division is",a/b)
#Function Declaration is done like this
def FuncDecl():
    pass

a=int(input("Enter a large number "))
b=int(input("Enter a small number "))
AddFunc(a,b)
SubFunc(a,b)
MulFunc(a,b)
DivFunc(a,b)

#definition of function can be done later
def FuncDecl():
    print("FuncDecl Defined at the end")

#It has to be called after definition    
FuncDecl()