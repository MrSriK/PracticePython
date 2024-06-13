#All are Objects, not mere variables
a=1
b="one"
c=True
d=None
e=2.3
f=complex(9,4)
print(a," Datatype of a is ",type(a))
print(b," Datatype of b is ",type(b))
print(c," Datatype of c is ",type(c))
print(d," Datatype of d is ",type(d))
print(e," Datatype of e is ",type(e))
print(f," Datatype of f is ",type(f),"\n\n")
listOne=[1,2.3,True,[4,complex(5,3)],"apple"]   #Mutable i.e. Changes can be made or Mutations possible
print(listOne,"\n")
tupleOne=(1,(complex(3,8),False),"Mango") #Immutable i.e. Changes not allowed or Mutations Not allowed
print(tupleOne,"\n")
dictionary={'key':'value',1:'ubuntu','powerful':True} #Key-Value pairs
print(dictionary)