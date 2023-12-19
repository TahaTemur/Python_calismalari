sehirler = ['kocaeli','istanbul']
plakalar = [41,34]

print(plakalar[sehirler.index('istanbul')])

plakalar2 = {'kocaeli':41,'istanbul':34}

print(plakalar2['kocaeli'])
print(plakalar2['istanbul'])

users = {
    'sadikturan': {
        'age': 36,
        'roles': ['admin','user'],
        'email': 'sadik@gmail.com',
        'phone': 1234567,
        },
    'cinarturan': {
        'age': 2,
        'roles': ['ads','uss'],
        'email': 'cinar@gmail.com',
        'phone': 5678901,
        }
    }

print(users['cinarturan']['phone'])
print(users['sadikturan']['roles'])
print(users['sadikturan']['roles'][0])