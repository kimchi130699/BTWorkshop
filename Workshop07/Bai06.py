a = int(input('Nhap a:'))
b = int(input('Nhap b :'))
chan = []
le = []
count =0
count1 =0
for i in range(a,b+1):
    if i%2==0:
        chan.append(i)
        count +=1
    else:
        le.append(i)
        count1 +=1
print(chan , 'co',count,'so chan')
print(le,'co',count1,'so le')