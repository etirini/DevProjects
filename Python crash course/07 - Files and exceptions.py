#with abre y cierra el archivo file_object automaticamente. 
#rstrip() elimina la linea en blanco que se genera por read
#Si quisiera usar un path absoluto deberia usar \\ porque \ es un caracter de escape

#read() lee todo el archivo y lo devuelve como str
#readline() devuelve una linea en particular
#readlines() devuelve todas las lineas como una lista de strs

""" 
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

#Para retener el acceso al contenido de un archivo (como almacenarlo en una lista) se utiliza readlines()

with open('pi_digits.txt') as file_object2:
    lines = file_object2.readlines()
for line in lines:
    print(line.rstrip())

#eliminar la separacion entre las ineas para crear un string unico

with open('C:\\Users\\etiri\\Documents\\Python\\Python crash course\\pi_digits.txt') as file_object2:
    lines = file_object2.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
print(pi_string)
print(len(pi_string))

with open('C:\\Users\\etiri\\Documents\\Python\\Python crash course\\pi_million_digits.txt') as file_object2:
    lines = file_object2.readlines()
pi_string = ''
for line in lines:
    pi_string += line.rstrip()
bday = input('escribi tu cumple mmddaaaa ')
if bday in pi_string:
    print('lo encontramos')
else:
    print('no lo encontramos')


with open('C:\\Users\\etiri\\Documents\\Python\\Python crash course\\en_python.txt') as file_object3:
    lines = file_object3.readlines()
line_string = ''
for line in lines:
    line_string += line

with open('tu_vieja.txt', 'w') as tvj:
    tvj.write('tu vieja')

with open('tu_vieja.txt', 'a') as tvj:
    tvj.write('\ntu\n')
    tvj.write('vie\n')
    tvj.write('ja\n')


print('dame dos nums para dividir. q para salir')
while True:
    prim_num = input('primer numero ')
    if prim_num == 'q':
        break
    sec_num = input('segundo numero ')
    if sec_num == 'q':
        break
    try:
        ans = int(prim_num) / int(sec_num)
    except ZeroDivisionError:
        print('no no no nooo')
    else:
        print(ans)

try:
    with open('chuchu.txt', 'w', encoding='utf-8') as f:
        print(f)
except FileNotFoundError:
    print('no se encuentra el archivo')

def wordCounter(filename):
    try:
        with open(filename, encoding='utf-8') as f:            
            content = f.read()
    except FileNotFoundError:
            #print(f'The book {filename} could not be found')
            #en vez de reportar el error (como arriba) se puede hacer un silent fail (como abajo)
            pass 
    else:
        words = content.split()
        num_words = len(words)
        print(f'the book {filename} contains {num_words} words')


files = ['alice.txt', 'little_women.txt','moby_dick.txt', 'otro_libro.txt']
for filename in files:
    wordCounter(filename)


def confirma_si_numero(ingreso1, ingreso2):
    ingresos = [ingreso1, ingreso2]
    valoresASumar =  []
    for ingreso in ingresos:
        try:
            int(ingreso)
        except ValueError:
            pass
        else:
            valoresASumar.append(ingreso)
    ans = sum(valoresASumar)
    print(ans)

def file_reader(filename):
    try:
        with open(filename) as f:
            name = f.read()
            lines = name.rstrip()
    except FileNotFoundError:
        print(f'no se encontro el archivo {filename}')
    else:
        print(lines)


files_to_read = ['michis.txt', 'perris.txt', 'manaticis.txt']
for files in files_to_read:
    file_reader(files)

#se puede usar json para guardar y acceder informacion. 

numbers = [1,2,3,4,5,6,7,8,9]
with open('numbers.json', 'w') as f:
    json.dump(numbers, f)

with open('numbers.json') as f:
    numeros = json.load(f)
print(numeros)
"""


import json
def get_stored_username():
    filename = 'users.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_username():
    username = get_stored_username()
    
    check_username = input(f'Are you {username} y/n ')
    if check_username == 'n':
        get_new_username()
        
    else:
        
    #if username:
    #    print(f'welcome back {username}')
        print(f'Welcome back {username}')
       
def get_new_username():
    username = input('What is your name ')
    filename = 'users.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    print(f'we will remember you next time {username}')
    return username

greet_username()