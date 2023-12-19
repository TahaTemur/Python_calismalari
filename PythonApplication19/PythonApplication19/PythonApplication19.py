x,y,z = 9,18,22

x,y = y,x

x += 5
y -= 5
z *= 5
x /= 5
z %= 3
x //= 5
y **= 2

print(x,y,z)

values = 1,2,3 #daha fazla eleman konulursa hata verir yetersiz olur.

print(type(values))

x,y,z = values 

print(x,y,z)

#ustteki durum icin bu yapilir.

values = 1,2,3,4,5,6

print(type(values))

x,*y,z = values 

print(x,y,z)

x,y,*z = values 

print(x,y,z)



