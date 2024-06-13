fruit="Mango"
print(len(fruit))
#slicing ie to only print some of the characters specifically
print(fruit[0:]) #These 3 statements will give same output
print(fruit[:])
print(fruit[:5])
'''
The logic is to print from a certain Index to (N-1)th index characters
0th index i.e. M to (5-1)=4th index i.e. o
'''
print(fruit[1:4]) #will give us 1st index to 3rd index characters
print(fruit[0:-2]) #gives us 0th to ((len(fruit)-2)-1)th index ie 0 to (3-1)=2nd index characters
print(fruit[-1:-3])
'''
The above print will give no output as is it computed like
[len(fruit)-1 : len(fruit)-3] which is [4:2] making no sense for interpreter
'''
print(fruit[-3:-1])
'''
This however will print since the result is
len(fruit)-3 : len(fruit)-1 which is [2:4]
'''