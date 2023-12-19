x = 5
hak = 5
devam = 'e'

result = 5<x<10
print(result)

result2 = x>5 and x<10
print(result2)

result3  = hak>0 and devam=='e'
print(result3)

result4 = x > 0 or x%2==0
print(result4)

result5 = not(x>0)
print(result5)

#1- Girilen sayinin 0-100 arasinda olup olmadigini kontrol et.

a = float(input('Sayi: '))

b = a>0 and a<100
print(b)

#2- Girilen sayinin pozitif cift oldugunu kontrol et.
a = int(input('Sayi: '))

b = b > 0 and b%2==0
print(b)

#3- Email ve parola bilgileriyle giris kontrolu yap.
a = 'alihasanozankoc@gmail.com'
b = 'abc123'

c = input('email: ')
d = input('password: ')

e = (c==a) and (d==b.lower().strip())
print(f'Uygulamaya giris basarili mi?: {e}')

#4- Kisinin ad,kilo ve boy bilgilerini alip BKI lerini hesapla.
# Formul: (kilo/boyun karesi)
# 0-18.4 Zayif
# 18.5-24.9 Normal
# 25.0-29.9 Fazla kilolu
# 30.0< Obez

name = input('Adiniz: ')
kg = float(input('Kilonuz: '))
hg = float(input('boyunuz: '))

index = (kg) / (hg**2)
zayif = index>0 and index<=18.4
normal = index>18.4 and index<=24.9
fazla = index>25 and index<=29.9
obez = index>30

print(f'Sayin {name}, vucut kutle indeksin (BKI): {index} ve vucudun: {zayif}')
print(f'Sayin {name}, vucut kutle indeksin (BKI): {index} ve vucudun: {normal}')
print(f'Sayin {name}, vucut kutle indeksin (BKI): {index} ve vucudun: {fazla}')
print(f'Sayin {name}, vucut kutle indeksin (BKI): {index} ve vucudun: {obez}')

