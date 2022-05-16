"""
f = open('test.txt', 'r')
print(f.name)
print(f.mode)
f.close()
"""


#Abajo ejemplo usando un context manager


#with open('test.txt', 'r') as f:
    #f_content = f.read() #Devuelve todo el contenido del archivo
    #f_content = f.readlines() #Devuelve todo el contenido del archivo, pero dentro de una lista y cada renglon es un elemento junto con el \n
    #f_content = f.readline() #Lee de a un renglon. Uno por cada ejecucion consecutiva
    #print(f_content)
    #f.seek(0) #Empieza a leer desde el caracter especificado en el argumento

    #for line in f:          #Lee de a una linea y la imprime para evitar quedarse sin memoria en caso de archivos grandes
    #    print(line, end='') #el end='' se usa para especificar que el ultimo caracter sea nada en vez de \n
    
    #+++++++++++++++++++++++++++++OTRA FORMA+++++++++++++++++++++++++++++
    
    #f_content = f.read(10) #le pasamos como argumento la cantidad de caracteres a leer
    #print(f_content, end='')
    
    #+++++++++++++++++++++++++++++MEJORAMOS SOBRE LA FORMA ANTERIOR+++++++++++++++++++++++++++++
    #size_to_read = 10
    #    f_content = f.read(size_to_read)
    #    while len(f_content) > 0:
    #        print(f_content, end = '*')
    #        f_content = f.read(size_to_read)

 
