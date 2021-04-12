class Ten:
    name = 'minh tuan'
    def __init__(self,name=None):
        self.name = name 
Kimchi = Ten('kim chi')
print('%s Ten is %s' % (Ten.name,Kimchi.name))

Ten_ = Ten()
Ten_.name ='kim phuong'
print('%s Ten la %s'% (Ten.name,Ten_.name))