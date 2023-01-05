def fib(n):
    if n==0:
        return 0
    if n==-1:
        return 1
    if n in [1,2]:
        return 1
    if n==-2:
        return -1
    if n<=-3:
        return fib(n+2)-fib(n+1)
    if n>=3:
        return fib (n-1)+fib(n-2)


list1=[]
number = int (input ('input number - '))
for e in range (-number,number+1):
    list1.append(fib(e))
print(list1)