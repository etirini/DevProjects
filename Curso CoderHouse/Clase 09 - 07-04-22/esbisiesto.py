
#Para calcular un anio bisiesto se divide el anio entre 100 y entre 400. 
#Si el resultado de % de ambos es 0, entonces es bisiesto

#Creamos dos funciones, la primera saluda al usuario y pide el anio. 
#La segunda hace el calculo y retorna el resultado

def saludo():
    print("Por favor ingrese un anio a calcular")
    ingreso = int(input("Solo ingrese valores enteros "))
    calcular(ingreso)
    print("el anio ", calcular(ingreso))

def calcular(ingreso):
    if (ingreso % 400 == 0) and (ingreso % 100 == 0):
        return "es bisiesto"
    else: 
        return "no es bisiesto"

saludo()
