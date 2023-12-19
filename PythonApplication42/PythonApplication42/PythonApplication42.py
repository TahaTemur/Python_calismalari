# class
class Person:
     pass  
     # class attributes
     address = 'No information'
     # constructor (yapici metod)
     def __init__(self, name, year):
         # object attributes
         self.name = name
         self.birthyear = year
         print('init metodu calisti.')
     # methods
     def intro(self):
         print('Hello There. I am '+ self.name)

     def calculateAge(self):
         return 2022 - self.birthyear
# object(instance)
p1 = Person(name = 'ali', year = 1990)
p2 = Person(name = 'yagmur', year = 1995)

p1.intro()
p2.intro()

print(f'adim: {p1.name} ve yasim: {p1.calculateAge()}')
print(f'adim: {p2.name} ve yasim: {p2.calculateAge()}')


class Circle:
     # class object attribute
     pi = 3.14
     # constructor (yapici metod)
     def __init__(self,yaricap=1):
         # object attributes
         self.yaricap = yaricap
     # methods
     def cevre(self):
         return 2*self.pi + self.yaricap

     def alan(self):
         return self.pi * (self.yaricap**2)

c1 = Circle() # yaricap = 1
c2 = Circle(5)

print(f'c1: alan = {c1.alan()} cevre = {c1.cevre()}')
print(f'c2: alan = {c2.alan()} cevre = {c2.cevre()}')