class hinhchunhat:
    def __init__(self,chieudai,chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong
    def kc(self):
        return self.chieudai
    def kc1(self):
        return self.chieurong
    def show(self):
        print('chieu dai:',self.chieudai)
        print('chieurong:',self.chieurong)
chieudai = int(input('chieu dai hcn:'))
chieurong = int(input('chieu rong hcn:'))
