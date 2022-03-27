numeros = [1,3,6,9]
ingreso = int(input("Ingrese un numero entre 0 y 9 "))
while ingreso not in range (0,10):
    ingreso = int(input("Debe ingresar un numero entre 0 y 9 unicamente "))
else:
    if ingreso in numeros:
        print("El valor se encuentra en la lista")
    else:
        print("El valor no se encuentra en la lista")

