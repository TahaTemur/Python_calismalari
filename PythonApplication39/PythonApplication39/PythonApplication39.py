
x = 'global x'

def function():
    x = 'local x'
    print(x)
function()
print(x)





name = 'Cinar'

def changeName(new_name):
    name = new_name
    print(name)
changeName('Ada')
print(name)





def greeting():
    name = 'Cinar'

    def hello():
        name = 'Ada'
        print('Hello '+ name)

    hello()

greeting()





x = 50
def test(x):
    print(f'x: {x}')

    x = 100
    print(f'changed x to {x}')
test(x)
print(x) # Burada fonksiyon disinda x yine 50 cikar.





x = 50
def test():
    global x
    print(f'x: {x}')

    x = 100
    print(f'changed x to {x}')
test()
print(x) # Bu sefer fonksiyon disinda x 100 cikar. *global x* fonksiyonu ile.
