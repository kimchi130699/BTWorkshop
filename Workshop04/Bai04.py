dic = {}
s = input('nhap chuoi:')

for a in s:
    dic[a] = dic.get(a,0)+1
print('\n'.join(['%s,%s' %(k,v) for k,v in dic.items()]))