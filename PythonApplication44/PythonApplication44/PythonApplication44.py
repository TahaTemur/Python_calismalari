myList = [1,2,3]
myString = 'my string'

print(len(myList))
print(len(myString))
print(type(myList))
print(type(myString))

class Movie():
    pass

m = Movie()

print(type(m))
# print(len(m)) Burada uzunluk olcemeyiz. Tip uygun degil len metodu yok.


class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie objesi olusturuldu.')
    
    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print('Film objesi silindi.')

m = Movie('Film adi','Yonetmen adi',120)

print(myList)
print(m)

print(str(myList))
print(str(m))

print(len(myList))
print(len(m))

#del m
#print(m) bu iki seyi yazarsak m silinir ve program m i tanimlanmamis gorup hata verir.