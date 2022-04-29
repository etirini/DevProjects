"""
def divi(a,b):

    if b==0:
        return None
    return print(a/b)
"""

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