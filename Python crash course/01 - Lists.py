#Crear una lista []
from time import perf_counter


bikes = ['mountain', 'fixed', 'specialized', 'redline', 'race']
print(bikes)

#Access elements in list
print(bikes[0])
print(bikes[0].title())

#Access last element in list, whatever the number of elements
print(bikes[-1])

#Accessing element in list + concatenation in string + formated 
message = f'My first bike was a {bikes[0].title()} bike.'
print(message)

#Reemplazando un objeto de lista via indice
bikes[0] = 'dual'
print(bikes)

#Agregando elemento via append (al final)
bikes.append('Triathlon')
print(bikes)

#Agregando elemento a lista via insert (indice + elemento)
bikes.insert(2, 'esa con la rueda gigante')
print(bikes)

#Borrar elemento con del 
del bikes[2]
print(bikes)

#eliminar el ultimo elemento en una lista con pop y utilizarlo en otra lista
print(bikes)
bikes_deleted = bikes.pop()
print(bikes)
print(bikes_deleted)

#eliminar un elemento en index especifico con pop y mandarlo a otra lista
print(bikes)
bikes_deleted = bikes.pop(1)
print(bikes)
print(bikes_deleted)

#eliminar un elemento por valor
bikes = ['mountain', 'fixed', 'specialized', 'redline', 'race']
print(bikes)
bikes.remove('fixed')
print(bikes)

#Ordenar alfabeticamente una lista permanentemente
tuvieja_sellama = ['clarita', 'amanda', 'ursula', 'ramona', 'josefina', 'maria']
tuvieja_sellama.sort()
print(tuvieja_sellama)

#SAME pero con orden inverso
tumama = ['a', 'b', 'c', 'z']
tumama.sort(reverse=True)
print(tumama)

#Ordenar alfabeticamente d emanera temporal con funcion Sorted() / tambien acepta reverse
letras = ['s','a', 'b', 'c', 'z','m','h','l','p','o','j']
print(sorted(letras))
print(letras)
print(sorted(letras,reverse=True))

#Imprimir lista en orden inverso (no alfabeticamente sino por orden de aparicion inverso)
letras.reverse()
print(letras)

#Longitud de lista
print(len(letras))

#Recorrer una lista con FOR
for letra in letras:
    print(letra)

numeros = list()
for value in range (1, 343):
    print(value)

#Creando una lista de valores con Range
numeritos = list(range(1,101))
print(numeritos)

#Usando range para crear una lista de solo pares y hacerlos al cuadrado
squares = []
for value in range(2,15,2):
    square = value **2
    squares.append(square)
print(squares) 

#Mismo ejemplo pero eliminando variable temporal para hacer el codigo mas conciso
squares = []
for value in range(2, 15, 2):
    squares.append(value **2)
print(squares)

#Funciones min max y sum para listas
print(min(squares))
print(max(squares))
print(sum(squares))

#List comprehension. Generando listas con expresiones en una sola linea
squares = [value**2 for value in range(1,15,2)]
print(squares)

#Slicing a list
players = ['jose', 'pedrito', 'maria', 'chuchu', 'cacha cacha', 'lalalala', 'pucho', 'virgocho' ]
print(players[:3])
print(players[3:5])
print(players[5:])

print("estos son los primeros tres de la lista")
for player in players[:3]:
    print(player.title())

#Copiando una lista. Crear una copia es distinto a asignar una variable a otra ( x = y) porque de esa manera apuntarian a la misma lista. 
#Esto es crear una lista independiente de la que parte.
mis_comidas = ['pizza', 'milanesas', 'rissotto', 'poshito']
copia_mis_comidas = mis_comidas[:]
copia_2 = mis_comidas
mis_comidas.append('pure')
print(mis_comidas)
print(copia_mis_comidas)

#Tuples: Son listas que no se pueden modificar una vez creadas. (aunque se puede reasignar la variable )
pero_que_tuple = (1,2,3)
print(pero_que_tuple[0])

pero_que_tuple = (4,5,6)
print(pero_que_tuple[0])
#Las tuples son definiadas por la presencia de una coma. Los parentesis se agregan para hacerlas mas faciles de distinguir 

quesoi_t = 3,
quesoi_n = 3
quesoi_p = (3)
quesoi_pt = (3,)
print(type(quesoi_t)) #tuple
print(type(quesoi_n)) #int
print(type(quesoi_p)) #int
print(type(quesoi_pt)) #tuple

