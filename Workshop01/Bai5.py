import math

def songuyen(n):
    if (n<0):
        return False
    is_sn = int(math.sqrt(n))
    for  i in range(2,is_sn+1):
        if (n % i == 0):
            return False
    return True

n = int(input('nhap n:'))
print('tat ca nguyen to nho hon', n , 'la: ')
ls = "";
if (n >= 2):
    ls = ls + '2' + ' '
for i in range(3, n+1):
    if(songuyen(i)):
        ls = ls + str(i) + ' '
    i = i + 2
print(ls)
