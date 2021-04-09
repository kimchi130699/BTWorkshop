
n = int(input('Nhap so nguyen n = '))
tong = 0
for i in range(1,n+1):
    tong += i/(i+1)

print(round(tong,2))
