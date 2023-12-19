name = 'Sadik Turan'

for letter in name:
    if letter == 'u':
        break
    print(letter)

for letter in name:
    if letter == 'u':
        continue
    print(letter)

x = 0

while x<5:
    if x == 2:
        break
    print(x)
    x += 1

x = 0
while x<5:
    x += 1
    if x == 2:
        continue
    print(x)

x = 1
top = 0
while x<=100:

    top += x
    x += 1
  
    print(f'Toplam: {top}')

x = 1
top = 0
while x<=100:

    x += 1

    if x % 2 == 1:
        continue

    top += x
  
    print(f'Toplam: {top}')