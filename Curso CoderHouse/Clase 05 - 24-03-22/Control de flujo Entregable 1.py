#Nota importante. La consigna esta mal escrita. Mirar punto 4. Falta el menu division y no se entiende bien por que.
#1. Mostrar una suma de los dos números
#2. Mostrar una resta de los dos números(el primero menos el segundo)
#3. Mostrar una multiplicación de los dos números
#4. Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará
#En caso de no introducir una opción válida, el programa informará de que no es correcta.



prim_num = float(input("Ingrese el primer numero "))
seg_num = float(input("Ingrese el segundo numero "))
operacion = int(input("Ingrese el numero de la operacion que desea realizar \n 1. Sumar \n 2. Restar \n 3. Multiplicar \n 4. Dividir \n 5. Salir \n "))
resultado = float("inf")


while operacion in range (1, 6): 
    if operacion == 1:
        resultado = prim_num + seg_num
        print(resultado)
        break
    elif operacion == 2:
        resultado = prim_num - seg_num
        print(resultado)
        break
    elif operacion == 3:
        resultado = prim_num * seg_num
        print(resultado)
        break
    elif operacion == 4:
        resultado = prim_num / seg_num
        print(resultado)
        break
    elif operacion == 5:
        print("Selecciono salir. Gracias")
        break 
else:
    print("Opcion invalida. Saliendo")
