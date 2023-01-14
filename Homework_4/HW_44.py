def Cf(k):
    lst = ''
    for i in range (0,k+1):
        koef = random.randint(0,100)
        if (koef!=0) and (i<k+1-2):
            lst = lst+str(koef)+'*x'+'^'+str(k-i)+' + '
    koef = random.randint(0,100)
    if (koef!=0) and (k>0):
        lst = lst+str(koef)+'*x'+' + '
    koef = random.randint(0,100)
    if (koef!=0):
        lst = lst+str(koef)+ ' = 0'
    return(lst)        
        
import random
m = int(input('input k - '))
mstr = str(m)
data = open('file44.txt','a')
data.writelines('k='+ mstr +' => ' + Cf(m)+'\n')
data.close