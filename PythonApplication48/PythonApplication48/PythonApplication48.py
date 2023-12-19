
# Error Handling = Hata Yonetimi

try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)

except ZeroDivisionError:
    print('y icin 0 girilemez.')

except ValueError:
    print('x ve y icin sayisal deger girmelisiniz.')

except (ZeroDivisionError,ValueError) as e:
    print('Yanlis bilgi girdiniz.')
    print(e)



while True:

    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)

    except Exception as ex:
        print('Yanlis bilgi girdiniz.',ex)
    else:
        break
    finally:
        print('try except sonlandi.')


# x = 10

# if x>5:
    # raise Exception('x 5 den buyuk deger alamaz.')

def check_password(psw):
    import re
    if len(psw) < 8:
        raise Exception('Parola en az 7 karakter olmalidir.')
    
    elif not re.search('[a-z]',psw):
        raise Exception('Parola kucuk harf icermelidir.')
    
    elif not re.search('[A-Z]',psw):
        raise Exception('Parola buyuk harf icermelidir.')
    
    elif not re.search('[0-9]',psw):
        raise Exception('Parola rakam harf icermelidir.')
    
    else:
        print('Gecerli parola')

password = input('')

try:
    check_password(password)

except Exception as ex:
    print(ex)
else:
    print('Gecerli parola: else')
finally:
    print('Validation completed.')


