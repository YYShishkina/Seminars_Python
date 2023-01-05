list1 = [1.1,1.2,3.1,5.1,10.01]
list2 = []
print(list1)
for i in range (0,len(list1)):
        list2.append(int(list1[i]))
        list2[i]=round((list1[i]-list2[i]),3)
print(list2)  
max = list2[1]
min = list2[1]
for i in range (1,len(list2)):
        if max < list2[i]:
            max =list2[i]
        if min > list2[i]:
            min = list2[i]
print(max-min)
   