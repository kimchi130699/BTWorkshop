class Circle():
    def __init__(self,r):
        self.radius = r

    def Area(self):
        return self.radius**2*3.14
r = int(input('Nhap r :'))
S = Circle(r)
print('Area = 'S.Area())