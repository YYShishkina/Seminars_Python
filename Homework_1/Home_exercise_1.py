numb_day = int (input ('input number day of the week - '))
if (numb_day<=0 or numb_day>=8):
    print (' in week only 7 days, tray again')
if (numb_day>=1 and numb_day<=5):
    print ('it is work day')
if (numb_day==6 or numb_day==7):
    print ('it is weekend')
    