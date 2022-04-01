

#Sets

grupo = {'Miguel', 'Blanca', 'Mario', 'Andres'}
print(grupo)
grupo.update(['Ana', 'Ramon', 'Marta', 'Erica', 'David'])
grupo.discard('Ana')
print(grupo)

#Diccionarios
nombres_alumnos = {'Primero' : 'Esteban', 'Segundo' : 'Stefania'}
print(nombres_alumnos)
#No son indexados pero si son ordenados por insercion. Python recuerda en que orden se ingresaron. 
#Es mutable mediante insercion por key (clave)
nombres_alumnos["Primero"] = "Sebastian"
print(nombres_alumnos)

