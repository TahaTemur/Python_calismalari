fruits = {'orange','apple','banana'}

# print{fruits[0]} indekslenemez.


fruits.add('cherry')
fruits.update(['mango','grape','apple']) #liste icine ikinci ayni elemani eklemez.

for x in fruits:
    print(x)

fruits.remove('mango')
print(fruits)
fruits.discard('apple')
print(fruits)
fruits.pop() # Silinecek elemani belirtmezsek listenin son elemani silinir.
print(fruits)
fruits.clear()
print(fruits)

myList = [1,2,5,5,4,4,2,1]
print(myList)
print(set(myList))