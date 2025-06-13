# https://docs.python.org/3/library/time.html#time.strftime

import time
t = time.strftime('%H:%M:%S')
# print(timestamp)
hour = int(time.strftime('%H'))
print(hour)

# timestamp3 = int(time.strftime('%M'))
# print(timestamp3)
# timestamp4 = int(time.strftime('%S'))
# print(timestamp4)

if (hour >=0 and hour < 12):
    print("Good Morning Sir! ")
elif (hour > 12 and hour <= 5):
    print("Good Afternoon Sir! ")
else:
    print("Good Night Sir")
