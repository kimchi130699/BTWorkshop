def function( n,b ):
    if (n<0 or b<2 or b>16):
        return ''
    sb = ''
    c = 0
    a = n 
    while (a > 0):
        if b > 0:
            m = n%b
            if m>10:
                sb = sb + str(chr(55+ a))
            else:
                sb = sb +str(c)
        else:
            sb = sb + str(a%c)
        a =int(a/b)
    return ''.join(reversed(sb))
n = int(input('nhap so nguyen duong n :'))
print('he so co 2 cua so nguyen ', n ,' la :' , function(n,2))
print('he so co 16 cua so nguyen ', n ,' la :' , function(n,16))

