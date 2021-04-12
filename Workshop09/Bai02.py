n = int(input('Nhap n :'))
def kimchi(n):
    i = 0
    while i<n :       
        i +=1
        if i%7 == 0:
            yield i 

for i in kimchi(n):
    print(i)
