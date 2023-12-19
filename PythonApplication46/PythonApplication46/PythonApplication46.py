import math

value = math.sqrt(49)
value2 = math.factorial(5)
value3 = math.floor(5.9)
value4 = math.ceil(5.9)
value5 = math.fabs(-2)

print(value)
print(value2)
print(value3)
print(value4)
print(value5)

from math import factorial,sqrt,ceil

def sqrt(x):
    print('x: '+ str(x))

print(value)


# example

import random

result = random.random()
result = random.random()*100
result = int(random.uniform(10,100))
result = random.randint(1,100)

greeting = 'Hello there'
names = ['ali','yagmur','deniz','cenk','ahmet','efe']

result = names[random.randint(0,len(names)-1)]
result2 = random.choice(names)
result3 = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)

liste2 = range(100)
result4 = random.sample(liste2,3)
result5 = random.sample(names,2)

print(liste)
print(result)
print(result2)
print(result3)
print(result4)
print(result5)