from operator import itemgetter, attrgetter
# Bài tập Python 22 Code by Quantrimang.com
l = []
s = input()

for i in s:
    l.append(tuple(s.split(",")))

print (sorted(l, key=itemgetter(0,1,2)))