
list = [1,2,3]

for item in list:
    print(item)

for item in range(10):
    print(item)

for item in range(5,50):
    print(item)

for item in range(5,50,5):
    print(item)




# enumerate

index = 0
greeting = 'Hello There'

for letter in greeting:
    print(f'index: {index} letter: {letter}')
    index += 1

for item in enumerate(greeting):
    print(item)
   
for index,item in enumerate(greeting):
    print(f'index: {index} letter: {item}')


# zip

list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)

print(list(zip(list1,list2,list3)))
