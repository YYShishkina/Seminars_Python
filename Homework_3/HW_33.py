number = int (input ('input number - '))
list1 = []
list2 = []
if number == 0:
    print (0)
else:
    while number>=1:
        list1.append(int(number%2))
        number = number/2
    #print(list1)
    list1.reverse()
    print(list1)
#for i in range (0, len(list1)):
#    list2.append(list1(len(list1)-i-1))
    
    
        

    
    
    
    