maasAli = 5000
maasAhmet = 4000
vergi = 0.27

print(maasAli - (maasAli * vergi))
print(maasAhmet - (maasAhmet * vergi))

# Degisken Tanimlama Kurallari

# 1- rakam ile baslayamaz.
# 1number olmaz. number1 olabilir.

# 2- bir degisken tanimlandiginda tekrar kullanilamaz.

number1 = 10
print(number1)

number1 = 20
print(number1)

number1 += 30
print(number1) #sonuc 50 olur. 20+30

# 3- buyuk kucuk harf onemlidir.

age = 20
AGE = 30

print(age)
print(AGE)

# 4- turkce karakter kullanilmaz.
x = 1 # int
y = 2.3 # float
name = "Cinar" # string
isStudent = True # bool

x, y, name, isStudent = (1, 2.3, "Cinar", True)
a = '10'
b = '20'
print(a+b) # 30 olmaz --> 1020

firstName = "Sadik"
lastName = "Turan"

print(firstName + lastName) # Sadýk Turan