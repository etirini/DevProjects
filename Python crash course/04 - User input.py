# Controlando input con un while
"""
prompt = 'decime algo mieja'
prompt +='\no escribi salir para salir '
message = ''
while message != 'salir':
    message = input(prompt)
    if message != 'salir':
        print(message)

#controlando input con while y flag
prompt = 'decime algo mieja'
prompt += '\no escribi salir para salir '
active = True
while active:
    message =input(prompt)
    if message == 'salir':
        active = False
    else: 
        print(message)

#terminando un loop con break
prompt = 'decime algo mieja'
prompt += '\no escribi salir para salir '

while True:
    message = input(prompt)
    if message == 'salir':
        break
    else:
        print(message)

#Usando Continue para ejecutar una condicion sin salir del while

current = 0
while current < 10:
    current += 1
    if current % 2 == 0:
        continue
    print(current)


#loop y modificar un dict. con while
unconfirmed_users = ['user1', 'user2', 'user3', 'user4' ]
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Confirming user: {current_user.title()}")
    confirmed_users.append(current_user)

print('The following users have been confirmed')
for confirmed_users in confirmed_users: 
    print(confirmed_users.title())

#remove all instances of an element from list
pets = ['cat', 'dog', 'fish', 'ferret', 'bird', 'dog', 'dog']
print(pets)

while 'dog' in pets:
    pets.remove('dog')

print(pets)

#filling dictionary w/user input





responses = {}
polling_active = True

while polling_active:
    name = input("Por favor ingrese su nombre ")
    response = input("de que ciudad proviene ese nombre")

    responses[name] = response 

    new_poll = input("Queda alguien por responder (s/n) ")
    if new_poll == 'n':
        polling_active = False
    
for name, response in responses.items():
    print(f'el nombre {name} proviene de {response}')

alumnos = {}
flag = True

while flag:
    
    nombre = input(f'\nDecime tu nombre')
    apellido = input(f'\nDecime tu apellido')


    alumnos[nombre] = apellido

    contar_otro = input(f'\nHay algun otro alumno para ingresar? (s/n) ')
    if contar_otro == 'n':
        flag = False
    

for nombre, apellido in alumnos.items():
    print(f'\n el alumno {nombre} {apellido} esta presente')


destinos = {}
lugares_prohibidos = ['area 51', 'triangulo', 'norcorea']

continuar = True

while continuar:
    cliente = input('Decime tu nombre ')
    destino = input('Donde te gustaria viajar? ')
    if destino in lugares_prohibidos:
        destino = input('ese lugar esta prohibido, elegi otro ')
    else:
        destinos[cliente] = destino

    mas_destinos = input('queres agregar otro destino? (s/n)')
    if mas_destinos == 'n':
        continuar = False

for cliente, destino in destinos.items():
    print(f'{cliente} quiere ir a {destino}')

"""

