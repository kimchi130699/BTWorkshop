# a = int(input())
# b = int(input())
# def uscln(a, b):
#     if (b == 0):
#         return a
#     return uscln(b, a%b)
# print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b))
def uscln(a, b):
    temp1 = a;
    temp2 = b;
    while (temp1 != temp2):
        if (temp1 > temp2):
            temp1 -= temp2;
        else:
            temp2 -= temp1;
    uscln = temp1;
    return uscln;
a = int(input("Nhập số nguyên dương a = "));
b = int(input("Nhập số nguyên dương b = "));
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b));

with open('Bai01.txt','w') as f:
	print(uscln(a,b) , file=f)