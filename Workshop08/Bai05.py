def nguyento(n):
    count = 0
    for i in range(1, n+1):
        if n%i ==0:
            count+=1
    if count == 2:
        return True
    return False
n = int(input('Nhap so nguyen n : '))
print(nguyento(n))



# n = int(input('Nhap so nguyen n :'))
# if n<1:
#     print(n,'ko phai la nguyen to')
# else:
#     if n%2 == 0:
#         print(n,'ko phai la nguyen to')
#     else:
#         print(n,'la so nguyen to')


