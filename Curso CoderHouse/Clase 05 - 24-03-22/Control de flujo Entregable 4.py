cantidad = int(input("Ingrese la cantidad de numeros a calcular "))
lista = []
for numeros in range(cantidad):
    pos_val = 1
    cta = print(f"Ingrese el numero {pos_val} de {cantidad}")
    numero = int(input())
    lista.append(numero)
    pos_val = pos_val + 1 
media = sum(lista) / cantidad
print(f"la media es {media}")


