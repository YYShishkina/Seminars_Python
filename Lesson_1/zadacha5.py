a = float(input('input number - '))
print(int(a*10%10))

b = input('input second number - ')
for i in range (1, len(b)):
    if b[i]=='.':
        print (int(b[i+1]))