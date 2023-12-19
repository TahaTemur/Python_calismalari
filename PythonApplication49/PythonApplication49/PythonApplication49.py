
# PYTHONDA DOSYA OKUMA VS ISLEMLERI


# Dosya acmak ve olusturmak icin open() fonksiyonu kullanilir.
# Kullanimi: open(dosya_adi,dosya_erisme_modu)


# dosya_erisme_modu dosyayi hangi amacla actigimizi belirtir.

# 1- 'w': (write) yazma modu. Dosyayi konumda olusturur.

# ORNEK: file = open('newfile.txt','w',encoding='utf-8')
# (encoding= 'utf=8' turkce karakterler de kullanilabilsin diye kullanilir.)

       # file = open('C:/users/ali/desktop/newfile.txt','w')
       # file.close()



# 2- 'a': (append) Dosya konumda yoksa olusturur.

# ORNEK: with open('newfile.txt','a',encoding='utf-8') as file:
       # file.write('\nEmel Turan')
       # with open('newfile.txt','r',encoding='utf-8') as file:
       # file.write('deneme')
       # Dosyada olmayan emel turan bilgisini eklemis olur.



# 3- 'x': (create) Dosya zaten varsa hata verir. Olusturmaya yarar.



# 4- 'r': (read) Okuma. Dosya konumda yoksa hata verir.

# with komutu: open() in basina gelir (read kullanilirken.) if else gibi blok olusturur.
# Okunan dosyayi okuduktan sonra kapatirken ise yarar.

# ORNEK: with open('newfile.txt','r',encoding='utf-8') as file:
       # content = file.read()
       # print(content)
       # file.seek(0) # seek imleci konumlandirir.
       # print(file.tell()) # tell imlecin nerede oldugunu soyler.
       # content2 = file.read()
       # print(content2)



# ONEMLI: with open('newfile.txt','r+',encoding='utf-8') as file:
    # file.write('deneme')

    # # with open('newfile.txt','r+',encoding='utf-8') as file:
    # print(file.read()) 

# yaparsak guncellemis oluruz. 0. indexten itibaren bir kez deneme yazar 
# fakat ayni seyi w ile yapsaydik icerigi siler sadece deneme yazardi.



# ONEMLI: with open('newfile.txt','r+',encoding='utf-8') as file:
    # file.seek(20)
    # file.write('deneme')

# with open('newfile.txt','r+',encoding='utf-8') as file:
    # print(file.read())

# 20.karakterden itibaren deneme yazar.



# ONEMLI: with open('newfile.txt','r+',encoding='utf-8') as file:
       # content = file.read()
       # content = 'Efe Turan\n' + content
       # file.seek(0)
       # file.write(content)
       # with open('newfile.txt','r+',encoding='utf-8') as file:
       # print(file.read())
# Sayfa basinda guncelleme yapar.



# ONEMLI: with open('newfile.txt','r',encoding='utf-8') as file:
       # list = file.readlines()
       # list.insert(1,'Ali Korkmaz')
       # file.seek(0)
       # for i in list:
       #     file.write(i)
# with open('newfile.txt','a',encoding='utf-8') as file:
# print(file.read())

# Sayfa ortasinda guncelleme yapar.