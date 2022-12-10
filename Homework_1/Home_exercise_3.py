x = int (input ('input X - '))
y = int (input ('input Y - '))
if (x==0 or y==8):
    print ('point is located on the axis')
if (x>0 and y>0):
    print ('point in the first quarter')
if (x<0 and y>0):
    print ('point in the second quarter')
if (x<0 and y<0):
    print ('point in the third quarter')
if (x>0 and y<0):
    print ('point in the forth quarter')