class kimchi():
    def __init__(self):
        self.s = "" 
    def getstr(self):
        self.s = str(input())
    def printstr(self):
        print(self.s.upper())
kim_chi = kimchi()
kim_chi.getstr()
kim_chi.printstr()
