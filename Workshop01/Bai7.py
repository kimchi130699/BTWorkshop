import math 

def songuyen(n):
    if (n<2):
        return False
    is_sn = int(math.sqrt(n))
    for i in range(2, is_sn + 1):
        if (n % i == 0):
            return False
    return True
print('liet ke cac so nguyen co 5 chu so :')
dem = 0
for i in range(10001,99999):
    if (songuyen(i)):
        print(i)
        dem = dem + 1
print('Tong cac so nguyen co 5 chu so la :', dem)