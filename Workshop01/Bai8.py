def fibonacci(n):
    f0 = 0
    f1 = 1
    fn = 1
    
    if (n<0):
        return -1
    elif (n == 0 or n == 1):
        return n
    else :
        for i in range(2,n):
            f0 = f1
            f1 = fn
            fn =f0+f1

        return fn
print('10 so dau tien cua day so fibonacci la :')
ls =''
for i in range(0,10):
    ls = ls + str(fibonacci(i)) + ','
print(ls)