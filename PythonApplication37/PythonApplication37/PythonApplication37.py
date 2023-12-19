
#1- Gonderilen kelimeyi istenen kez ekranda gosteren fonksiyonu ekrana yaz.

def yazdir(kelime,adet):
    print(kelime * adet)

yazdir('Merhaba\n',10)


#2- Kendine gonderilen sinirsiz parametreyi bir listeye ceviren fonksiyonu yaz.

def listeyeCevir(*params):
    liste = []

    for param in params:
        liste.append(param)

    return liste

result = listeyeCevir(10,20,30,'Merhaba')
print(result)


#3- Gonderilen 2 sayi arasindaki tum asal sayilari bul.

a = int(input('1.Sayi: '))
b = int(input('2.Sayi: '))

def asal(a,b):
    for sayi in range(a,b+1):
        if sayi > 1:
            for i in range(2,sayi):
                if(sayi % i==0):
                    break
            else:
                print(sayi)

asal(a,b)


#4- Kendisine gonderilen bir sayinin tam bolenlerini bir liste seklinde dondur.

def tamBolenleriBul(a):
    tamBolenler = []

    for i in range(2,a):
        if(a %i==0):
            tamBolenler.append(i)

    return tamBolenler

a = int(input('Tam Bolenleri Bulunacak Sayi: '))
print(tamBolenleriBul(a))
