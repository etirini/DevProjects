#El numero de ej. es 6 cuando deberia ser 7
#Me parece que esta solucion es re cabeza, pero es la unica que se me ocurre. 


lista_1 = ["h", 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
lista_2 = ["h", 'o', 'l', 'a', ' ', 'l', 'u', 'n', 'a']
lista_3 = []

for letras_1 in lista_1:
    for letras_2 in lista_2:
        if letras_1 == letras_2:
            while letras_1 not in lista_3:
                lista_3.append(letras_1)
print(lista_3)
