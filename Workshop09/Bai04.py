def sochan(n):
    lst =[]
    for i in range(n):
        if i%2==0:
            lst.append(i)
            return True
        return False
filter_ = filter(sochan,lst)
print (sochan(0,1,2,3,4))
        