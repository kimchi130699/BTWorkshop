n = int(input('Nhap do dai n:'))
lst = []
for i in range(n):
    lst.append(int(input()))
min_value = lst[0]
for i in lst:
    if i < min_value:
        min_value = i
print(lst)
print(min_value)