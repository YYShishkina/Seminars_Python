lst = [3, 1, 5, 6, 7, 5, 7, 8]
lstRez = []
counter = 0
for i in range (0,len(lst)):
    for j in range (0, len(lst)):
        if (lst[i] == lst[j]) and (i!=j):
            counter = counter+1 
    if counter == 0:
        lstRez.append(lst[i])
    counter = 0
print(lstRez)        