n = int(input('nhap do dai n :'))
lst =[]
for i in range(n):
    lst.append(int(input()))
tong = 0
for j in lst:
    tong += j
print(tong)