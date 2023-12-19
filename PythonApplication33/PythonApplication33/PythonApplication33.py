# ASAL SAYI BULMA KODU

sayi = int(input('Sayi: '))
asalmi = True

if sayi == 1:
    print('Asal sayi degildir.')

for i in range(2,sayi):
    if(sayi % i==0):
        asalmi = False
        break
if asalmi:
    print('Sayi asaldir.')
else:
    print('Sayi asal degildir.')