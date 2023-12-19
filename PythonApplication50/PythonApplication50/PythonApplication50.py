
def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    
    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])

    ort = (not1+not2+not3)/3

    if ort>=90 and ort<=100:
        harf = 'AA'
    elif ort>=80 and ort<90:
        harf = 'BA'
    elif ort>=70 and ort<80:
        harf = 'BB'
    elif ort>=65 and ort<70:
        harf = 'CB'
    elif ort>=60 and ort<65:
        harf = 'CC'
    elif ort>=50 and ort<60:
        harf = 'DD'
    elif ort>=30 and ort<50:
        harf = 'FD'
    elif ort>=0 and ort<30:
        harf = 'FF'
    else:
        print('Hatali sayi girdiniz.')

    return ogrenciAdi+ ': '+harf+'\n'
    
def ort_oku():
    with open('sinav_notlari.txt','r',encoding = "utf-8") as file:
        for satir in file:
            print(satir)

def not_gir():
    ad = input('Ogrenci adi: ')
    soyad = input('Ogrenci soyadi: ')
    not1 = input('1.Not: ')
    not2 = input('2.Not: ')
    not3 = input('3.Not: ')

    with open('sinav_notlari.txt','a',encoding = "utf=8") as file:
        file.write(ad+' '+soyad+':'+not1+','+not2+','+not3+'\n')

def not_kaydet():
    with open('sinav_notlari.txt','r',encoding = "utf-8") as file:
        liste = []

        for i in file:
            liste.append(not_hesapla(i))

        with open('sonuclar.txt','w',encoding = "utf-8") as file2:
                  file2.write(i)

while True:
    islem = input('1- Notlari Oku\n2- Not Gir\n3- Notlari Kaydet\n4- Cikis\n')

    if islem == '1':
        ort_oku()
    elif islem == '2':
        not_gir()
    elif islem == '3':
        not_kaydet()
    else:
        break