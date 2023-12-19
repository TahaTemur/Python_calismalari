
#1- "Bmw,Mercedes,Opel,Mazda" elemanlariyla bir liste olustur.
list1 = ['Bmw','Mercedes','Opel','Mazda']
print(list1)

#2- Liste kac elemanlidir?
result = len(list1)
print(result)

#3- Listenin ilk ve son elemani nedir?
result = list1[0]
result2 = list1[-1]
print(result)
print(result2)

#4- Mazda yerine Toyota yazdir.
list1[-1] = 'Toyota'
print(list1[-1])

#5- Mercedes listenin bir elemani midir?
result = 'Mercedes' in list1
print(result)

#6- Listenin -2 indeksindeki deger nedir?
result = list1[-2]
print(result)

#7- Listenin ilk 3 elemanini yazdir.
result = list1[0:3]
result2 = list1[:3]
#bu 2 si aynidir.

print(result)
print(result2)

#8- Listenin son 2 elemani yerine "Toyota ve Renault" yazdir.
list1[-2:] = ['Toyota','Renault']
result = list1
print(result)

#9- Listeye "Audi ve Nissan" ekle.
a = list1 +['Audi','Nissan']
print(a)

#10- Listenin son elemanini sil.
del list1[-1]
print(list1)

#11- Liste elemanlarini tersten yazdir.
result = list1[::-1]
print(result)

#12- Asagidaki verileri listeye al.

# studentA: Yigit Bilgi 2010, (70,60,70)
# studentB: Sena Turan 1999, (80,80,70)
# studentC: Ahmet Turan 1998, (80,70,90)

sA = ['Yigit','Bilgi',2010,[70,60,70]]
sB = ['Sena','Turan',1999,[80,80,70]]
sC = ['Ahmet','Turan',1998,[80,70,90]]

print(sA)
print(sB)
print(sC)

#13- Liste elemanlarini ekrana yazdir.

result = sA[0]
result2 = sB[1]
result3 = sC[3][1]
result4 = f"{sA[0]} {sA[1]} {2022-sA[2]} yasinda ve not ortalamasi {(sA[3][0] + sA[3][1] + sA[3][2])/3}"
result5 = f"{sB[0]} {sB[1]} {2022-sB[2]} yasinda ve not ortalamasi {(sB[3][0] + sB[3][1] + sB[3][2])/3}"
result6 = f"{sC[0]} {sC[1]} {2022-sC[2]} yasinda ve not ortalamasi {(sC[3][0] + sC[3][1] + sC[3][2])/3}"

print(result)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)