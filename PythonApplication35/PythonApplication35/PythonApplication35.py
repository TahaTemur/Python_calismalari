def sayHello():
    print('Hello')
sayHello()


def sayHello(name):
    print('Hello '+ name)

sayHello('Ali')
sayHello('Ayse')


def sayHello(name = 'user'):
    print('Hello '+ name)
    
sayHello('Ali')


def sayHello(name = 'user'):
    return 'Hello '+ name

msg = sayHello('Cinar')
print(msg)


def total(a,b):
    return a+b
c = total(10,20)
d = total(40,50)
print(c,d)


def yas(dogumyili):
    return 2022 - dogumyili

ageAli = yas(2002)
ageYigit = yas(2010)

print(ageAli,ageYigit)


def emekli(dogumyili,isim):
    age = yas(dogumyili)
    emekli = 65 - age

    if emekli>0:
        print(f'Emekliliginize {emekli} yil kaldi.')
    else:
        print('Zaten emekli oldunuz.')

emekli(2002,'Ali')