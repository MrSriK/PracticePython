name="Sivaramakrishnan"
for x in name:
    print(x,end="+")
    if(x=="a" or x=="i"):
        print("New Line now\n")

fruits=['apple','banana','orange','mango','grapes']
for f in fruits:
    print(f," is spelled as")
    for i in f:
        print(i)

for i in range(5): #Starts from 0 and ends at 5-1=4, same as range(0,5,1)
    print(i)

print("\n")
for i in range(1,10): #Starts from 1 and ends at 9, same as range(1,10,1)
    print(i)

print("\n")
for i in range(1,100,10): #Starts from 1, then next iteration it jumps to 1+10=11, so on till the end range
    print(i)