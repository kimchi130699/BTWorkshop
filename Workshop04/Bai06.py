def diction():
    d = dict()
    for i in range(1,4):
        d[i] = i**2
    for k,v in d.items():
        print(k,':',v)
print(diction())