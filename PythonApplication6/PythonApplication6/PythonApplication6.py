
name = 'Cinar'
surname = 'Turan'
age = 36
print('My name is {0} {1}' .format(name, surname))
print('My name is {1} {0}' .format(name, surname))
print('My name is {s} {n}' .format(n=name,s=surname))
print('My name is {} {} and I am {} years old' .format(name, surname,36))

result = 200/700
print('The result is {}'.format(result))
print('The result is {r:1.4}'.format(r=result))
# r:a.b a tam kisimdan once bosluk birakir. b ise virgulden sonra kac sayi yazdirilacak onu belirler.