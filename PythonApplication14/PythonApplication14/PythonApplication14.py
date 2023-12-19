list = [1,2,3]

tuple = (1,'iki',3)

print(type(list))
print(type(tuple))

print(list[2])
print(tuple[2])

list = ['ali','veli']
tuple = ('damla','kaya')

list[0] = 'ahmet'
print(list)

# tuple[0] = 'deniz'
# print(tuple) tuple list ile ayni mantik fakat icine list gibi deger eklenmez.

tuple = ('a','b','c')
g = ('d','e','f') + tuple

print(g)
