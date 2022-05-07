"""
def divi(a,b):

    if b==0:
        return None
    return print(a/b)


def divi(a,b):
    try:
        print(a/b)
    except ZeroDivisionError as zd:
        print("No se puede dividir entre 0")
    except Exception as e:
        print("Algo salio mal")
    finally:
        print("Saliendo")

divi(10,0)

def juntaprome(dias):
    try:
        contador = 1
        a = []
        while contador <= dias:
            prom = calcavgtemp()
            a.append(prom)
            contador += 1
        chadprom = sum(a)/dias    
        print(a)
        print(chadprom)
    except:
        print("Le chingaste")



def calcavgtemp():
    min = float(input("Ingrese temp minima "))
    max = float(input("Ingrese temp maxima "))
    prome = (min+max)/2
    return prome


juntaprome(3)

"""
a = 1
try:
    if int(a) == True:
        print("int")
    else: 
        print("nop")
except:
    print("Algo salio mal")

print(type (a) == int)

