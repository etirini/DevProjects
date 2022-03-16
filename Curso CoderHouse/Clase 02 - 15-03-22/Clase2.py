lista1 = ["Esta", "es una lista", "numero 1"]
lista2 = ["Otra", "lista"]

lista1.append(1234)
lista1.append("Hola")
lista2.append("adios")
lista2.append(1234)

lista3 = lista1[0:len(lista1)-1]
print(lista3)
lista4 = lista2[1:len(lista2)-1]
print(lista4)
lista5 = lista3 + lista4
print(lista5)
print(type(lista5))