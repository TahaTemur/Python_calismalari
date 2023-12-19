x = y = [1,2,3]
z = [1,2,3]

print(x==y)
print(x==z)
print(x is y)
print(x is z) # listeler ayni ama x ve z ya da y ve z is de true vermez.
# Onemli olan objeler ayni mi degil mi bu onemli. Ayni adres meselesi.

print('banana' in x)

name = 'Cinar'
print('a' in name)
print('b' not in name)