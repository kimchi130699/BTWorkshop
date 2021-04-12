# s = str(input('Nhap chuoi :'))
# hoa = []
# demhoa = 0
# thuong = []
# demthuong = 0
# for i in s :
#     if (i.isupper() == True):
#         hoa.append(i)
#         demhoa += 1
#     if (i.islower()):
#         thuong.append(i)
#         demthuong +=1
# print(hoa , demhoa)
# print(thuong,demthuong)

def kimchi(s):
    demhoa = 0
    demthuong = 0
    for c in s:
        if c.isupper():
            demhoa +=1
        if c.islower():
            demthuong +=1
    print(s)
    print(demhoa)
    print(demthuong)
s = str(input('Nhap chuoi :'))
kimchi(s)