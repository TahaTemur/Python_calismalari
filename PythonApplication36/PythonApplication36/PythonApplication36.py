def changeName(n):
    n = 'ada'

name = 'yigit'

changeName(name)
print(name)


sehirler = ['ankara','izmir']

def change(n):
    n[0] = 'istanbul'

change(sehirler)
print(sehirler)



def add(a,b):
    return sum((a,b))

print(add(10,20))

# c ye 0 verdik cunku c parametresine bir sey girilmezse hata verir ikili toplama yapilmaz.
# Yahut c yi koymadan uclu toplama yapamayiz. Bu mantikla son parametrelere 0 verilebilir.

def add(a,b,c=0):
    return sum((a,b,c))

print(add(10,20))
print(add(10,20,30))


def add(*params):
    return sum((params))

print(add(10,20,30,40,50))


def add(*params):
    sum = 0

    for n in params:
        sum += n
    return sum

print(add(10,20))
print(add(10,20,30,990))




def displayUser(**args): #tuple yerine dictionary olsun diye iki yildiz koyduk.
    for key,value in args.items():
        print('{} is {}'.format(key,value))

displayUser(name = 'Ali', age = 20, city = 'Istanbul')
displayUser(name = 'Hasan', age = 19, city = 'Ankara')
displayUser(name = 'Ozan', age = 18, city = 'Izmir')

def myfunc(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myfunc(10, 20, 30, 40, 50, 60, 70, key1 = 'value 1', key2 = 'value 2')