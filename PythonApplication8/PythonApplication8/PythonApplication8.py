
message = 'Hello There. My name is Sadik Turan'

message = message.upper()
message2 = message.lower()
message3 = message.capitalize()
message4 = message.title()
message5 = message.split()
message6 = message.strip()
message7 = '*'.join(message)
message8 = message.center(70,'*')

index = message.find('Sadikk') #pozitif deger cikarsa o ifade degiskende yer alir. negatifse yer almaz.
print(index)

isFound = message.startswith('H') #true verirse o harfle basliyordur. false ise baslamiyordur.
print(isFound)

isFound2 = message.endswith('n') #true verirse o harfle bitiyordur. false ise bitmiyordur.
print(isFound2)

print(message)
print(message2)
print(message3)
print(message4)
print(message5)
print(message6)
print(message[2])
print(message7)
print(message8)