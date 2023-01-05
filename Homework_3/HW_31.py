list1 = [2,3,5,6,5]
list2 = []
print(list1)
if len(list1)%2==0:
    for i in range (0,int(len(list1)/2)):
        m=list1[i]*list1[int(len(list1)-i-1)]
        list2.append(int(m))
else:
    for i in range (0,int(len(list1)/2+1)):
        list2.append(int(list1[i]*list1[int(len(list1)-i-1)])) 
print(list2)        
