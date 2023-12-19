# SAYI TAHMIN OYUNU
#** 1-100 arasinda rastgele uretilecek bir sayiyi asagi yukari ifadeleriyle bulmaya calis.
#** "random modulu" icin "python random" seklinde arama yap.
#** 100 uzerinden puanlama yap. Her soru 20 puan.
#** Hak bilgisini kullanicidan alin ve her soru belirtilen can sayisi uzerinden hesaplansin.

import random

sayi = random.randint(1,100) # Girilen araliktaki sayilardan rastgele birini secer.
can = int(input('Kac hak kullanmak istersiniz: '))
hak = can
sayac = 0

while hak>0:
    hak -= 1
    sayac += 1
    tahmin = int(input('Tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler {sayac}. defada bildiniz. Toplam puaniniz: {100 - (100/can)*(sayac-1)}')
        break # Oyun bittiginde donguden cikmak icin.
    elif sayi > tahmin:
        print('Yukari')
    else:
        print('Asagi')
