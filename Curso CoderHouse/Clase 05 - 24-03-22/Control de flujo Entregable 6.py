#La primera vez que hice este ej lo hice sin haber leido la aclaracion de "conversion a lista" (hasta habia puesto un comentario diciendo "Que quiere decir conversion de lista?")
#Despues vi el comentario asi que los hice de nuevo. La version con conversion de list esta entre los ********** y el nro de lista esta duplicado (11 en vez de 1, 22 en vez de 2, etc)


#Todos los números del 0 al 10 [0, 1, 2, ..., 10]
lista_1 = []
for numero in range (0, 11):
    lista_1.append(numero)
print(lista_1)


lista_11 = list(range (0, 11))
print(lista_11)
print("***************")


#Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
lista_2 = []
for numero in range(-10, 1):
    lista_2.append(numero)
print(lista_2)


lista_22 = list(range(-10, 1))
print(lista_22)
print("***************")


#Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
lista_3 = []
for numero in range(0, 21, 2):
    lista_3.append(numero)
print(lista_3)


lista_33 = list(range (0, 21, 2))
print(lista_33)
print("***************")


#Todos los números impares entre - 20 y 0 [-19, -17, -15, ..., -1]
lista_4 = []
for numero in range(-21, 0, 2):
    lista_4.append(numero)
print(lista_4)


lista_44 = list(range (-21, 0, 2))
print(lista_44)
print("***************")


#Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]
lista_5 = []
for numero in range(0, 51, 5):
    lista_5.append(numero)
print(lista_5)


lista_55 = list(range(0, 51, 5))
print(lista_55)
print("***************")
