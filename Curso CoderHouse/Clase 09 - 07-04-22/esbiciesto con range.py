#Creamos dos funciones, la primera saluda al usuario y pide el anio. 
#La segunda hace el calculo y retorna el resultado

def saludo():
    #print("Por favor ingrese un anio a calcular")
    ingreso = anios()
    while ingreso <= 4000:
    #print(ingreso)
        calcular(ingreso)
        print("el anio ", ingreso, calcular(ingreso))
        ingreso = ingreso +1


def calcular(ingreso):
    if (ingreso % 400 == 0) or (ingreso % 4 == 0) and (ingreso % 100 != 0):
        return "es bisiesto"
    else:
        return "no es bisiesto"

def anios():
    for anio in range(1,4000):
        return(anio)

saludo()
