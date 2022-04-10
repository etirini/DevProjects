from calendar import isleap

def saludo():
    ingreso = anios()
    while ingreso <= 4000:
        calcular(ingreso)
        print("el anio ", ingreso, calcular(ingreso))
        ingreso = ingreso + 1


def calcular(ingreso):
    if isleap(ingreso) == True:
        return "es bisiesto"
    else:
        return "no es bisiesto"


def anios():
    for anio in range(0, 4000):
        return(anio)


saludo()
