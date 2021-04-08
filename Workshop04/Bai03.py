def kotrung(li):
    lst = []
    x = set()
    for i in li:
        if i not in x:
            x.add(i)
            lst.append(i)
    return lst
li =[12,24,35,24,88,120,155,88,120,155]
print(kotrung(li))