website = 'http://www.sadikturan.com'
course = 'Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 Saat)'

#1- 'Hello World' un bas ve son karakterini silin.
result = ' Hello World '.strip()
result2 = ' Hello World '.lstrip()
result3 = ' Hello World '.rstrip()
print(result)
print(result2)
print(result3)

result4 = website.lstrip('/:pth')
print(result4)

#2- 'www.sadikturan.com' icindeki sadikturan haricindeki her karakteri silin. 
result = 'www.sadikturan.com'.strip('www.moc')
print(result)

#3- 'course' un tüm karakterlerini kucuk harf yapin.
result = course.lower()
print(result)

#4- 'website' icinde kac tane a vardir?
result = website.count('a')
print(result)

#5- 'website' www" ile baslayip com ile bitiyor mu?
result = website.startswith('http')
result2 = website.endswith('com')
print(result)
print(result2)

#6- 'website' icinde '.com' ifadesi var mi?
result = website.find('com')
result2 = website.find('com',0,10)
result3 = course.find('Python')
print(result)
print(result2)
print(result3)

#7- 'course' taki karakterlerin hepsi alfabetik mi?
result = course.isalpha()
result2 = course.isdigit() #hepsi rakam mi?
print(result)
print(result2)

result3 = '123'.isdigit()
print(result3)

#8- 'Contents' ifadesini satirda 50 karakter icine yerlestirip sagina ve soluna * ekleyiniz.
result = 'Contents'.center(50,'*')
result2 = 'Contents'.ljust(50,'*')
result3 = 'Contents'.rjust(50,'*')
print(result)
print(result2)
print(result3)

#9- 'course' taki tüm bosluk karakterlerini - ile degistirin.
result = course.replace(' ','-')
result2 = course.replace(' ','-',5)
result3 = course.replace(' ','')
print(result)
print(result2)
print(result3)

#10- 'Hello World' un 'World' kelimesini 'There' ile degistirin.
result = 'Hello World'.replace('World','There')
print(result)

#11- 'course' u bosluk karakterlerinden ayirin.
result = course.split(' ')
result2 = result[2] # indexte [] icine yazilan sayiya ait kelimeyi yazdir (ornegin 2 yazdik 3.kelime). 
print(result)
print(result2)

