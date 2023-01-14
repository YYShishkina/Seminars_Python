import HW_44
import random

m = int(input('input k - '))
mstr = str(m)
data_1 = open('file45_1.txt','a')
data_2 = open('file45_2.txt','a')
ur_1 = HW_44.Cf(m)
ur_2 = HW_44.Cf(m)

data_1.writelines('k='+ mstr +' => ' + ur_1+'\n')
data_2.writelines('k='+ mstr +' => ' + ur_2+'\n')
data_1.close
data_2.close
if len(ur_1)>=len(ur_2):
    for i in range (0, len(ur_1)):
        if ()        
else:
    for i in range (0, len(ur_2)):
        
        

a, lit1, b, lit2, c = ur_1[:-3].split()
b=lit1+b
c=lit2+c
a=int(a[:a.index('x')])
b=int(b[:b.index('x')])
c=int(c)