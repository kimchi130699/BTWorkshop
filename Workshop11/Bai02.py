class kimchi():
    def __init__(self):
        self.s = ''
    def getString(self):
        self.s = input()
    def printString(self):
        print(self.s.upper())
kimchi_ = kimchi()
kimchi_.getString()
kimchi_.printString()