
contador = 0
while contador < 10:
    print(f"Hola, el contador esta en {contador}")
    contador = contador + 1


cuenta = 20 
while cuenta >= 0:
    print(f"Lanzamiento en {cuenta}")
    cuenta = cuenta - 1 
    continue
else:
    print("Lanzamiento correcto")


alumno = ["fulano", "mengano", "sultano", "lontano"]

for nombre in alumno:
    print(f"el alumno se llama {nombre}")


for index, nombre in enumerate(alumno):
    print(f"el indice es {index}")
    print(f"el nombre es {nombre}")
numeros = range(10)

for numero in numeros:
    print(numero)
numeros = range(3, 30)

for numero in numeros:
    print(numero)
numeros = range(5, 30, 5)

for numero in numeros:
    print(numero)
