num = [1,3,5,7,9,12,19,21]

#1- num daki hangi sayilar 3 un katidir?
for nums in num:
    if(nums%3==0):
        print(nums)

#2- num daki sayilarin toplami?
top = 0
for nums in num:
    top += nums
    print(f'toplam: {top}') # ya da print('toplam: ',top)

#3- num daki tek sayilarin karesini al.
for nums in num:
    if(nums%2==1):
        print(nums**2)

sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

#4- sehirler den hangileri en fazla 5 karakterlidir?
for sehir in sehirler:
    if(len(sehir)<= 5):
        print(sehir)

urunler = [{'name':'Samsung Galaxy S6','price': '3000'},
           {'name':'Samsung Galaxy S7','price': '4000'},
           {'name':'Samsung Galaxy S8','price': '5000'},
           {'name':'Samsung Galaxy S9','price': '6000'},
           {'name':'Samsung Galaxy S10','price': '7000'}]

#5- urunler in fiyatlari toplami kac?
top = 0
for urun in urunler:
    fiyat = int(urun['price'])
    top += fiyat
    print('Toplam urun fiyati: ',top)
    print(f'Toplam urun fiyati: {top}')

#6- urunler den fiyati en fazla 5000 olan urunleri goster.
for urun in urunler:
    fiyat = int(urun['price'])
    if(fiyat<=5000):
        print(urun['name'])

