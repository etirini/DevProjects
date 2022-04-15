def rango(inicio, fin):
    if inicio == fin:
        print("Termino")
    else:
        rango(inicio + 1, fin)
        print(inicio)


rango(1, 10)

