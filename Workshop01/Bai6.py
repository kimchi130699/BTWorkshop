import math

def songuyen(n):
    if (n<2):
        return False
    is_sn = int(math.sqrt(n))
    for i in range(2, is_sn+1):
        if(n % i==0):
            return False
    return True            
n = int(input('Nhap n:'))
print(n,'so nguyen to dau tien la:')
dem = 0
i = 2
ls = ''
while (dem < n):
    if(songuyen(i)):
        ls = ls +str(i) + ' '
        dem = dem + 1
    i = i +1
print(ls)