x = int (input ('input number of quarter - '))
if (x<=0 or x>=5):
    print ('There is no quarter with this number') 
if (x==1):
    print ('Point coordinates will always X>0 and Y>0')
if (x==2):
    print ('Point coordinates will always X<0 and Y>0')
if (x==3):
    print ('Point coordinates will always X<0 and Y<0')
if (x==4):
    print ('Point coordinates will always X>0 and Y<0')