#OOP

# class
# instance (object)

lst = [1,2,3]

result = type(lst)

print(result)

# class
class Person:
     pass  
# attributes
# methods

# object(instance)
#p1 = Person()
#p2 = Person()

#print(p1)
#print(p2)
#print(type(p1))
#print(type(p2))
#print(p1==p2)

# class
class Person:
     pass  
     # class attributes
     address = 'No information'
     # constructor (yapici metod)
     def __init__(self, name, birthyear):
         # object attributes
         self.name = name
         self.birthyear = birthyear
         print('init metodu calisti.')
     # methods

# object(instance)
p1 = Person(name = 'ali', birthyear = 1990)
p2 = Person(name = 'yagmur', birthyear = 1995)

# updating
p1.name = 'ahmet'
p1.address = 'kocaeli'

# accessing object attributes
print(f'name: {p1.name} year: {p1.birthyear} address: {p1.address}')
print(f'name: {p2.name} year: {p2.birthyear} address: {p2.address}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))