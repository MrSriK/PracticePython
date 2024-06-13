for i in range(3):
    print(i)

#similar while loop
i=0
while (i<3):
    print(i)
    i+=1

j=0
while(j<=77):
    j=int(input("Enter a number: "))
    j+=1
print("Loop condition not met, exitted loop")

#ELse can also be usd with while loops. once while condition becomes false, interpreter comes to else part
i=0
while(i%2==0 and i<10):
    print(i)
    i=i+2
else:
    print("Inside Else part")

#Python does not have Do-While Loop, but we can emulate like this. The loop condition must execute at least once

i=0     #do part
print(i+1)
while(i<10):    #while part
    i=0
    print(i)