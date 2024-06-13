# Break Statements are for Skipping the loop
# Continue statements are for Skipping the Iteration
for i in range(20):
    if(i==10):
        print("Break Condition Matched...")
        break
    print("5 X",i,"=",5*i)
print("Exitted the Loop...")

print("\nContinue Demo...\n")
for i in range(21):
    if(i%2==0):
        print("Continue Condition Matched...")
        continue
    print("5 X",i,"=",5*i)
print("Exitted the Loop...\n")

#DO-while using Break, we need to use infinite while loop
i=0
while True:
    print(i)
    i+=1
    if(i%100==0):
        break