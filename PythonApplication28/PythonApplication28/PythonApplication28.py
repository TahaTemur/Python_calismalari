x = 0
while x<100:
    x += 1
    print(x)

x = 0
while x<=100:
    if x%2==1:
       print(f'sayi tek: {x}')
       x += 1
    else:
       print(f'sayi cift: {x}')
       x += 1
print('Bitti...')

name = ''
while not name.strip():
     name = input('Isminizi giriniz: ')
print(f'Merhaba {name}')

nums = [1,3,5,7,9,12,19,21]

#1- nums u while ile ekrana yazdir.
i = 0
while (i<len(nums)):
    print(nums[i])
    i += 1

#2- Kullanicidan iki sayi alip araligindaki tum tek sayilari ekrana yazdir.
a = float(input('Baslangic: '))
b = float(input('Bitis: '))

i = a
while i<b:
    i += 1
    if(i%2==1):
        print(i)

#3- 1-100 arasi tum sayilari azalan sekilde yazdir.
x = 100
while x>0:
     x -= 1
     print(x)

#4- Kullanicidan alinan 5 sayiyi sirali sekilde ekrana yazdir.
numbers = []
i = 0
while i<5:
    sayi = int(input('Sayi: '))
    numbers.append(sayi)
    i+=1
    numbers.sort()
    
print(numbers)
    
#5- Kullanicidan alinan sinirsiz urun bilgisini urunler listesi icinde sakla.
# Urun sayisini kullaniciya sor.
# dictionary listesi yapisi {name,price} olsun.
# urun ekleme bittiginde while ile ekrana listelensin.

urunler = []

adet = int(input('Kac urun eklemek istiyorsunuz: '))
i = 0

while(i<adet):
    name = input('Urun ismi: ')
    price = input('Urun fiyati: ')
    urunler.append({
        'name': name,
        'price': price,
    })
    i += 1

for urun in urunler:
    print(f'urun adi: {urun["name"]} urun fiyati: {urun["price"]}')

