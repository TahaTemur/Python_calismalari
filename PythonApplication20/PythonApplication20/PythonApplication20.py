x,y,z = 2,5,10

num = 1,5,7,10,6

#1- kullanicidan aldiginiz 2 sayinin carpimi ile x y z toplami farki nedir?

a = int(input('1.Sayi: '))
b = int(input('2.Sayi: '))

e = a*b - (x+y+z)
print(e)

#2- y nin x e kalansiz bolumu kactir?
f = y//x #veya f = int(y/x)
print(f)

#3- x y z toplaminin mod 3 u nedir?
g = (x+y+z)%3
print(g)

#4- y nin x inci kuvvetini hesaplayiniz.
h = y ** x
print(h)

#5- x,*y,z = num islemine gore z nin kupu kac?
num = 1,5,7,10,6
x,*y,z = num

i = z ** 3
print(i)

#6- x,*y,z = num islemine gore y nin degerleri toplami kac?
num = 1,5,7,10,6
x,*y,z = num

j = y[0] + y[1] + y[2]
print(j)
