# BANKAMATIK


SadikHesap = {
    'Ad': 'Sadik Turan',
    'HesapNo': '13245678',
    'Bakiye': 3000,
    'ekHesap': 2000,
}


AliHesap = {
    'Ad': 'Ali Koc',
    'HesapNo': '12345678',
    'Bakiye': 2000,
    'ekHesap': 1000,
}



def paracek(hesap,miktar):
    print(f'Merhaba {hesap["Ad"]}')

    if (hesap['Bakiye'] >= miktar):
        hesap['Bakiye'] -= miktar
        print('Paranizi alablirsiniz.')
        BakiyeSorgula(hesap)
    else:
        top = hesap['Bakiye'] + hesap['ekHesap']

        if(top >= miktar):
            ekHesapKullanimi = input('Ek hesap kullanilsin mi (e/h)')

            if ekHesapKullanimi == 'e':
                Bakiye = hesap['Bakiye']
                ekHesapKullanilacakMiktar = miktar - hesap['Bakiye']
                hesap['Bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Paranizi alabilirsiniz.')
                BakiyeSorgula(hesap)
            else:
                print(f'{hesap["HesapNo"]} nolu hesabinizda {hesap["Bakiye"]} bulunmaktadir.')
        else:
            print('Uzgunuz bakiye yetersiz.')
            BakiyeSorgula(hesap)

def BakiyeSorgula(hesap):
    print(f'{hesap["HesapNo"]} nolu hesabinizda {hesap["Bakiye"]} TL bulunmaktadir. Ek hesap limitiniz ise {hesap["ekHesap"]} TL.')



paracek(SadikHesap,3000)
BakiyeSorgula(SadikHesap)
print('************')
paracek(SadikHesap,2000)
BakiyeSorgula(SadikHesap)



paracek(AliHesap,750)
BakiyeSorgula(AliHesap)
print('************')
paracek(AliHesap,1500)
BakiyeSorgula(AliHesap)
