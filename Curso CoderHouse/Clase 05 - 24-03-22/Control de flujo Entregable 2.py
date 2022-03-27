
ingreso = int(input("ingrese un numero par "))
while (ingreso % 2 != 0):
    ingreso = int(input("Debe ingresar unicamente un numero par "))
else:
    print(f"El numero {ingreso} es par. Gracias")

