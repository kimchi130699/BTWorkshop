a = int(input('Nhap so a:'))
b = int(input('Nhap so b :'))
c = []
tong = 0
for i in range(a,b+1):
    if i %2!=0:
        c.append(i)    
        tong +=i
print(c)
print('Tong cua so le la :',tong)
