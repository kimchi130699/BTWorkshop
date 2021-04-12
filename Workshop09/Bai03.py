def kimchi(n):
    i = 0
    while i<=n:
        if i%2 ==0:
            yield i 
        i +=1

n = int(input('nhap n :'))
s = []
for i in kimchi(n):
    s.append(str(i))
print(','.join(s))

        

    
