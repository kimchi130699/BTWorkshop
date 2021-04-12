class hinhchunhat():
    def __init__(self,cd,cr):
        self.cd = cd 
        self.cr = cr 
    def area(self):
        return 'dien tich hinh chu nhat =', (self.cd*self.cr)
cd = int(input('nhap chieu dai:'))
cr = int(input('nhap chieu rong :'))
hcn = hinhchunhat(cd,cr)
print(hcn.area())