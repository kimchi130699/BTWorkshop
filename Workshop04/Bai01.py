s = str(input('Nhap chuoi:'))
x = [x for x in s.split(' ')]
print(' '.join(sorted(list(set(x)))))