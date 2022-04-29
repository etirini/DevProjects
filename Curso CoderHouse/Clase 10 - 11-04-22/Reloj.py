
def saludo(*args):
    if len(args) == 1:
        segundoAHoras(*args)
    elif len(args) == 3:
        horasASegundos(*args)
    else:
        print("La cantidad de valores no se puede procesar")

def segundoAHoras(args):
    user_select=args
    h = args / 3600
    m = (h%1)*60 # %1 "extrae" el decimal del mod h y eso multiplico por 60
    s = (m%1)*60 
    h_round = args // 3600
    m_round = round(m)
    s_round = s #esta fue la unica forma que se me ocurrio de hacer esta parte. Sorry si es muy caverna
    return print(f"{user_select} segundos equivalen a {h_round} horas {m_round} minutos y {s_round} segundos")

def horasASegundos(args):
    lista = [item for item in args]
    h=lista[0] * 60 * 60
    m=lista[1] * 60
    s=lista[2]
    suma = h + m + s
    return print(suma)

saludo(2,1,0)
saludo(7260)

