
ogrenciler = {
'120': {
        'ad': 'Ali',
        'soyad': 'Yilmaz',
        'tel': '532 000 00 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 00 02'
    },
    '128': {
        'ad': 'Volkan',
        'soyad': 'Yukselen',
        'tel': '532 000 00 03'
    }
}

#1- Bilgileri verilen ogrencileri kullanicidan aldiginiz bilgilerle dictionary icinde saklayin.

#2- Ogrenci numarasini kullanicidan alip ilgili ogrenci bilgisini gonderin.

ogrenciler = {}

num = input('Ogrenci no: ')
name = input('Ogrencinin adi: ')
sur = input('Ogrencinin soyadi: ')
phone = input('Ogrencinin telefonu: ')

#ogrenciler[num] = {
    #'ad': name,
    #'soyad': sur,
    #'tel': phone,
#}
#print(ogrenciler) asagidaki update metodu bu metodla ayni.

ogrenciler.update({
    num: {
        'ad': name,
        'soyad': sur,
        'tel': phone
        }
})

print('*'*50)

ogrNo = input('Ogrenci No: ')
ogrenci = ogrenciler[num]

print(f"Aradiginiz {ogrNo} nolu ogrencinin adi: {ogrenci['ad']} soyadi: {ogrenci['soyad']} ve telefonu ise {ogrenci['tel']}")




