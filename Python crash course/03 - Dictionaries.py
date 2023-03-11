
# Diccionario simple. Pensemos en un juego de aliens en el que cada alien tiene color y le corresponden puntos
alien_0 = {'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
print(alien_0['color'])
print(alien_0['points'])
Color_aliens = alien_0['color']
print(Color_aliens)

# Se puede definir un dic vacio y despues agregarle key pairs.
alien_1 = {}
alien_1['color'] = 'amarillo'
alien_1['puntos'] = 3
# print(type(alien_1))
print(alien_1)

# Modificar valores de un dict.
alien_0['color'] = alien_1['color']
print(alien_0['color'])

# Agregamos posibilidad de que el alien se mueva.
alien_0 = {'color': 'green', 'points': 5,
           'y_position': 25, 'x_position': 25, 'speed': 'medium'}
# mover el alien a la derecha
# determinar que tan lejos se puede mover el alien basado en su velocidad

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# nueva posicion en base a pos actual mas incremento
alien_0['x_position'] += x_increment
print(alien_0['x_position'])

# El metodo get permite obtener un valor de un key pair y muestra un error (no detiene ejecucion) en caso que el elemento no exista
planeta_origen = alien_0.get('planet', 'unknown origin')
assigned_points = alien_0.get('points', 'unknown points')
print(planeta_origen)
print(assigned_points)

# iterando diccionarios
fav_langs = {
    'juanita': ['c', 'c++', 'perl', 'rust'],
    'pedro': ['python', 'ruby', 'micropython'],
    'maria': ['c++', 'rockstar'],
    'lulu': ['visual basic'],
    'barbara': ['sql'],
    'edu': ['sql']
}

for ppl, lan in fav_langs.items():
    print(f'El lang favorito de {ppl.title()} es {lan.title()}')

# iterar keys es el comportamiento default de python
for key in fav_langs.keys():
    print(f'la key {key.title()} existe en el diccionario')

if 'esteban' not in fav_langs.keys():
    print('esteban responde la pregunta!')
if 'juanita' in fav_langs:
    print('muy bien juanita')

for key in sorted(fav_langs.keys()):
    print(f'{key.title()} gracias por responder las preguntas')

for langs in fav_langs.values():
    print(f'se menciono al lenguaje {langs.title()}')
print('\n')
# se puede usar set() para eliminar duplicados de una lista
for langs in set(fav_langs.values()):
    print(f'se menciono al lenguaje {langs.title()}')

# lista de diccionarios

#alien_0 = {'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
#alien_1 = {'color': 'yellow', 'points': 15, 'y_position': 55, 'x_position': 0}
#alien_2 = {'color': 'orange', 'points': 25, 'y_position': 75, 'x_position': 0}

#aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#    print(alien)

# creando aliens en bulk
print('\n bulking aliens')
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5,
                 'y_position': 25, 'x_position': 0}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'pink'
    print(alien_number)
    print(aliens[:3])

print(f'se crearon {len(aliens)} aliens')

# Lista en un diccionario
pizza = {
    'crust': 'thick',
    'toppings': ['kesito', 'huevo duro', 'salame']
}

print(f'La pizza tiene')

for topping in pizza['toppings']:
    print(f"\t {topping}")


for ppl, langs in fav_langs.items():
    print(f'{ppl} prefiere programar en ')
    for lang in langs:
        print(f'\t{lang}')


# diccionario en diccionario
users = {
    'aeinstein': {
        'name': 'albert',
        'lastname': 'einstein',
        'location': 'princeton'
    },
    'ntyson': {
        'name': 'neil',
        'lastname': 'tyson',
        'location': 'nose'
    }
}

for username, userinfo in users.items():
    print(f'usuario {username}')
    info = f"{userinfo['name']} {userinfo['lastname']}"
    print(info)


fav_city_stuff = {
    'miguel': {
        'berlin': {
            'food': 'schnitzel',
            'band': 'rammastein',
            'thing': 'walk the wall'
        },
        'chicago': {
            'food': 'pizza',
            'band': 'taylor swift',
            'thing': 'wall street'
        }
    },
    'brayan': {
        'buenos aires': {
            'food': 'milanesa',
            'band': 'bersuit',
            'thing': 'puerto madero'
        },
        'sydney': {
            'food': 'cangaroo bbq',
            'band': 'men at work',
            'thing': 'land down under'
        }
    }
}


for people, city in fav_city_stuff.items():
    print(f'{people}')
    for city in fav_city_stuff.items():
        print({city})


fav_city_thing = {
    'fulano': {
        'food': 'schnitzel',
        'thing': 'bikes',
    },
    'mengano': {
        'food': 'chori',
        'thing': 'lager'
    }
}

for people, activity in fav_city_thing.items():
    # print({people})
    actividad = {activity['food']}
    print(activity)
