website = 'http://www.sadikturan.com'
course = 'Python Kursu: Bastan Sona Python Programlama Rehberiniz (40 Saat)'

#1- 'course' karakter dizisinde kac karakter bulunmaktadir?
result = len(course)
length = len(website)

#2- 'website' icinden www karakterlerini alin.
result = website[7:10]
print(result)

#3- 'website icinden com karakterlerini alin.
result = website[22:25]
result = website[length-3:length]
print(result)

#4- 'course' icinden ilk ve son 15 karakteri alin.
result = course[0:15]
result = course[:15]
print(result)
# yukaridaki ikisi ayni

result = course[-15:]
print(result)



#5- 'course' ta ifadeleri tersten yazdir.
result = course[::-1]
#result = course[::x] x e ne koyarsaniz o siradaki karakteri almayacaktir. 
#ifadeyi tersten yazdiracaksak bosluk veya 1 degil -1 yazariz.
print(result)



name,surname,age,job = 'Bora','Yilmaz',32,'muhendis'

#6-Yukarda verilen degiskenlerle ('Benim adim Bora Yilmaz,yasim 32 ve meslegim muhendis') yazdir.
result = 'Benim adim '+name+ ' '+surname+',yasim'+str(age)+'ve meslegim'+job
result = 'Benim adim {} {}, yasim {} ve meslegim {}.' .format(name,surname,age,job)
result = f'Benim adim {name} {surname}, yasim {age} ve "meslegim" {job}.'
print(result)

#7- 'Hello world' ifadesindeki w harfini 'W' ile degistirin.
s = 'Hello world'
s = s[0:6] + 'W' + s[-4:]

print(s)

#8- 'abc' ifadesini yan yana 3 defa yazdirin.
result = ' abc ' * 3
print(result)
