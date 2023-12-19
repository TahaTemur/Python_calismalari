def usalma(number):

    def inner(power):
        return number ** power

    return inner

two = usalma(2)
three = usalma(3)

print(two(3))
print(three(3))





def yetkisorgulama(page):
    def inner(role):
        if role == 'Admin':
            return '{0} rolunun {1} sayfasina ulasabilir.'.format(role,page)
        else:
            return '{0} rolunun {1} sayfasina ulasamaz.'.format(role,page)
    return inner

user1 = yetkisorgulama('Product Edit')
print(user1('Admin'))
print(user1('User'))





def islem(islemadi):

    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim

    if islemadi == 'toplama':
        return toplam
    else:
        return carpma

toplama = islem('toplama')
print(toplama(1,3,5,6,7))

carpma = islem('carpma')
print(carpma(1,3,5,6,7))





def top(a,b):
    return a+b
def cikar(a,b):
    return a-b
def carp(a,b):
    return a*b
def bol(a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi == 'toplama':
        print(f1(6,3))
    elif islem_adi == 'cikarma':
        print(f2(6,3))
    elif islem_adi == 'carpma':
        print(f3(6,3))
    elif islem_adi == 'bolme':
        print(f4(6,3))
    else:
        print('Gecersiz islem...')

islem(top,cikar,carp,bol,'toplama')
islem(top,cikar,carp,bol,'cikarma')
islem(top,cikar,carp,bol,'carpma')
islem(top,cikar,carp,bol,'bolme')