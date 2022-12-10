x = int (input ('input number of day in the week - '))
if (x<=0 or x>=7):
    print ('The input number is wrong. In the week only seven days. Try again') 
if (x>=1 and x<=5):
    print ('Today is work day')
if (x==6 or x==7):
    print ('Today is weekend')