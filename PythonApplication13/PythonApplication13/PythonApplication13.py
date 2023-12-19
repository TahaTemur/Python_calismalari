names = ['Ali','Yagmur','Hakan','Deniz']
years = [1998,2000,1998,1987]

#1- 'Cenk' ismini liste sonuna ekle.
names.append('Cenk')
print(names)

#2- 'Sena' ismini liste basina ekle.
names.insert(0,'Sena')
print(names)

names.insert(-1,'Mehmet')
print(names)

names.insert(len(names),'Mehmet')
print(names)

#3- 'Deniz' ismini siliniz.
names.remove('Deniz')
print(names)

#4- 'Hakan' isminin indeksi nedir?
index = names.index('Hakan')
print(index)

#5- 'Ali' listenin bir elemani midir?
result = 'Ali' in names
print(result)

result = names.index('Ali')
print(result)

#6- Liste elemanlarini ters cevir.
names.reverse()
print(names)

#7- Liste elelmanlarini alfabetik olarak sirala.
names.sort()
print(names)

#8- years listesini rakamsal buyukluge gore sirala.
years.sort()
print(years)

#9- str = 'Chevrolet,Dacia' karakter dizisini listeye cevir.
str = 'Chevrolet Dacia'
result = str.split()
print(result)

#10- years in en buyuk ve en kucuk elemani nedir?
min = min(years)
max = max(years)
print(max,min)

#11- years in kac tane 1998 degeri vardir?
result = years.count(1998)
print(result)

#12- years in tum elemanlarini sil.
years.clear()
print(years)

#13- Kullanicidan alacaginiz 3 tane marka bilgisini bir listede sakla.
markalar = []

marka = input('Marka: ')
markalar.append(marka)

marka = input('Marka: ')
markalar.append(marka)

marka = input('Marka: ')
markalar.append(marka)

print(markalar)


