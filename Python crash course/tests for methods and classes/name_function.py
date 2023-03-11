#seteando un entorno en el que vamos a probar una funcion

#primero creamos la funcion, esta toma un nombre y un apellido y los devuelve formateados

def get_formatted_name(first, last, middle=''):    
    if middle:
        full_name = f'{first} {middle} {last}'
    else:
        full_name = f'{first} {last}'
    return full_name.title()

