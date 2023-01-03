number = input ('Enter number - ')
sum = 0
for i in range (0, len(number)):
    if (number[i]!='.'):
        sum= float(number[i])+sum
print ('Sum all digits in number is - ', sum)
    
