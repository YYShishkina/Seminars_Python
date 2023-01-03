import datetime

time = str(datetime.datetime.now())
Rand = 0
for i in range (len(time)-3,len(time)):
    Rand = Rand+int(time[i])
print ('random number - ', Rand)


