#En este ejemplo se busca el valor bmw, si existe lo imprime en mayusculas, se continua iterando la lista y se imprimen todos los otros valore que no son 
# bmw con una mayuscula

cars = ['bmw', 'audi', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.capitalize())

#keyword in para verificar si un valor existe en una lista
print('audi' in cars) #true
print('ford' not in cars) #true
print('bmw' not in cars) #false

#if elif else
age = 4
if age < 4:
    price = 0
elif age < 18:
    price = 12
else:
    price = 40

print(f"el precio a pagar es {price}")

#Evaluar multiples condiciones. Se hace en diferentes if statemens simples sin elif.
if 'bmw' in cars:
    print('veeemeeee')
if 'audi' in cars:
    print('la audi-acia de esta perra')
if 'ford' in cars:
    print('fofofofofoooooooooooooooooord')

#Verificando que lista no este vacia
requested_toppings = ['kesito']
if requested_toppings:
    for requested in requested_toppings:
        print(f"agregando {requested}")
    print("Terminamos de hacer tu pizzita")
else: 
    print('seguro que la quere vacia?')

#Usando dos listas.

avail_toppings = ['kesito', 'papeta', 'huevito', 'morro', 'camaro']
requested_toppings = ['kesito', 'anana', 'cangrejeto', 'anochoita']

for requested_topping in requested_toppings:
    if requested_topping in avail_toppings:
        print(f'agregando {requested_topping}')
    else:
        print(f'No tenemo {requested_topping}')
print('terminamo')
