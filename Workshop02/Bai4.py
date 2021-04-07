s1 = str(input('nhap s1:'))
s2 = str(input('nhap s2:'))

s0 = s1[0:2] + s2[2:]
s1 = s2[0:2] + s1[2:]
s2 = s0
print(s1)
print(s2)