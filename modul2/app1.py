"""
Get from input 23:30:31
Get from input 23:31:31

find difference between the 2 inputs in seconds
"""

time1 = input("Get time1: ")
hours1 = int(time1[0:2])
print('Time1 hours:', hours1)
minutes1 = int(time1[3:5])
print('Time1 minutes:', minutes1)
seconds1 = int(time1[6:8])
print('Time1 seconds:', seconds1)

time2 = input("Get time2: ")
hours2 = int(time2[0:2])
print('Time2 hours:', hours2)
minutes2 = int(time2[3:5])
print('Time2 minutes:', minutes2)
seconds2 = int(time2[6:8])
print('Time2 seconds:', seconds2)

t1 = 3600 * hours1 + 60 * minutes1 + seconds1
t2 = 3600 * hours2 + 60 * minutes2 + seconds2
print('Time difference in seconds:', t2 - t1)
