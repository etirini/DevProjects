""" 
nombre = input('ingresa tu nombre ')
print(f'buen dia {nombre} tu visita quedo guardada')

with open('guestbook.txt', 'a' ) as guests:
    guests.write(nombre + '\n')

"""
continuar = True
while continuar:
    nombre = input('ingresa tu nombre ')
    with open('guestbook.txt', 'a') as guests:
        guests.write(nombre + '\n')
    if nombre == '!':
        continuar = False
