number = int(input ('Enter N - '))
list =[]
for i in range (-number,number+1):
    list.append(i)
print('Create new list from - N to N:')
print (list)
path = 'NP.txt'
data = open(path,'r')
list2 =[]
for line in data:
    i=int(line)
    list2.append(i)
print('Numbers from file:')
print(list2)
data.close()
list3=[]
for i in range (0, len(list2)):
    list3.append(list[list2[i]-1])
print('The numbers from list with numbers from file:')
print(list3)
