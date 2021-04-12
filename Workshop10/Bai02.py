import math
def ptrinh(a,b,c):
    if a == 0:
        if b == 0:
            print('phuong trinh vo nghiem')
        else :
            x1 = -c/b
            print('Phuong trinh co 1 nghiem : ',x1)
        return
    if a != 0 :
        d = b**2 - 4*a*c
        if d< 0:
            print('phuong trinh vo nghiem')
        if d==0:
            x1 = -b/(2*a)
            print('phuong trinh co nghiem kep x1 = x2 = ',x1)
        if d > 0:
            x1 = (-b + math.sqrt(d))/(2*a)
            x2 = (-b - math.sqrt(d))/(2*a)
            print('phuong trinh co ngiem x1 = ',x1)
            print('phuong trinh co nghiem x2 =',x2)
    return
a = float(input('nhap so a :'))
b = float(input('nhap so b : '))
c = float(input('nhap so c :'))
ptrinh(a,b,c)

