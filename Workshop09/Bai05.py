a = [1,2,3,4,5,6,7,8,9,10]
lst = list(map(lambda x:x **2,filter(lambda x:x%2==0,a)))
print(lst)

# def kc(x):
#     for i in x:
#         if i%2==0:
#             return True
#         return False
# def kimchi(x):
#     for i in x:
#         return i**2
# print(list(map(kc,filter(kimchi,[0,1,2,3,4,5,6,7,8,9,10,11]))))




        