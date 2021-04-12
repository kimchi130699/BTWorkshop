class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self,a):
        Shape.__init__(self)
        self.lenght = a 
    def area(self):
        return self.lenght**2
c = int(input('Nhap canh a = '))
Square1= Square(c)
print(Square1.area())

