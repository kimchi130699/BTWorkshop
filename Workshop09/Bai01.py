def tong(n):
    if n ==1:
        return 1
    return n+tong(n-1)
n = int(input('Nhap n:'))
tong_n = tong(n)
print('Tong la:',tong_n)