
def my_decorator(func):
    def wrapper(name):
        print('Fonksiyondan onceki islemler')
        func(name)
        print('Fonksiyondan sonraki islemler')
    return wrapper

@my_decorator # @my_decorator ile sayHello func yerine gonderilir.
def sayHello(name):
    print('Hello',name)
sayHello('Ali')





import math
import time

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print('fonksiyon ' + func.__name__ + ' ' + str(finish-start) + ' '+ ' saniye surdu.')
    return inner

@calculate_time
def usalma(a,b):
    print(math.pow(a,b))
@calculate_time
def faktoriyel(num):
    print(math.factorial(num))

usalma(2,3)
faktoriyel(6)