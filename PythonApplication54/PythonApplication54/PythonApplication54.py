
liste2 = [6,7,8,9,10]
iterator = iter(liste2)

while True:
    try:
        element = next(iterator)
        print(element)

    except StopIteration:
        break





class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = MyNumbers(20,50)

myiter = iter(list)

while True:
    try:
        element = next(myiter)
        print(element)
    except StopIteration:
        break





generator = [i**3 for i in range(1,11)]
print(generator)

generator = (i**3 for i in range(1,11))
print(generator)

for i in generator:
    print(i)