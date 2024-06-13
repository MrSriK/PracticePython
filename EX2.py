import time
now=time.strftime('%H:%M:%S')
curr_hour=int(time.strftime('%H'))
print("Curretn time is",now)
if(curr_hour>5 and curr_hour<12):
    print("Good Morning Sir")
elif(curr_hour>11 and curr_hour<16):
    print("Good Afternoon Sir")
elif(curr_hour>15 and curr_hour<22):
    print("Good Evening Sir")
else:
    print("Good Night Sir")