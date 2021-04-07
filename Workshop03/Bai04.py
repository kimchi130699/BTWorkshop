n = int(input('Nhap do dai n :'))
lst = []
for i in range(n):
    lst.append(int(input()))
values = []
for i in lst:
    if (i%2 != 0):
        values.append(int(i))
if len(values) ==0 :
    values = [0]
print(lst)
print(values)