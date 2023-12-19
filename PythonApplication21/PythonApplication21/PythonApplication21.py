a,b,c,d = 5,5,10,4

result = a==b #a b ye esit demektir true veya false sonucu verir.
print(result)

password = '1234'
username = 'sadikturan'

result2 = ('sdktrn'==username)
print(result2)

result3 = a>c 
print(result3)

#1- Girilen 2 sayidan hangisi buyuktur?
a = int(input('1.Sayi: '))
b = int(input('2.Sayi: '))

c = a>b
print(f'a: {a} b: {b} den buyuktur: {c}')

#2- Eger ortalama 50 ve ustundeyse gecti degilse kaldi yazdir.
a = float(input('1.Vize: '))
b = float(input('2.Vize: '))
c = float(input('Final: '))

d = ((a+b)/2)*0.6 + c*0.4

print(f'Not ortalamaniz: {d} ve dersten gecme durumunuz: {d>=50}')

#3- Girilen sayinin tek mi cift mi oldugunu yazdir.
a = int(input('Sayi: '))

b = (a%2==0)

print(f'Girilen sayi cifttir: {b}')

#4- Girilen bir sayinin negatif veya pozitif oldugunu yazdir.
a = int(input('Sayi: '))

b = (a>0)

print(f'Sayi pozitif: {b}')

#5- Parola veya email bilgisini isteyip dogrulugunu kontrol et.

email = 'email@sadikturan.com'
password = 'abc123'

email1 = input('email: ')
password1 = input('parola: ')

isEmail = (email == email1)
isPassword = (password == password1.lower().strip())
#lower kucuk harfe duyarliligi kaldirir (buyuk harfler kuculur.).
#strip ise sifreden sonra yanlislikla girilen bosluklar yerine sadece girilen karakterlere odaklanir.

print(f'Email bilgisi dogru mu?: {isEmail} ve parola dogru mu?: {isPassword} ')

