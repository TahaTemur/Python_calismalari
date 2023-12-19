username = 'sadikturan'
password = '1234'

if 3>2:
   print('Hos geldiniz')



isLoggedin = False
if isLoggedin: # false true ya esit olmadigi icin buradan sonuc cikmaz.
     print('Hos geldiniz')
     


isA = (username == 'sadikturan') and (password == '1234')

if (username == 'turan'):
    if (password == '1234'):
        print('Hos geldiniz.')
    else:
        print('Parola yanlis.')
else:
    print('username yanlis.')



x = float(input('x: '))
y = float(input('y: '))

if x > y:
    print('x y den buyuk')
elif x == y:
    print('x ve y esit')
else:
   print('y x den buyuk')