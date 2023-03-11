
"""
# Positional arguments
# Arguments passed in a function where the position of each determines the invoke order

def describe_pet(animal_type, pet_name):
    print(f"my pet is a {animal_type} and it's name is {pet_name}")

describe_pet('dog', 'chuchu')

# Keyword argument
# it's a value pair where the argument and it's value are specified thus eliminating the need to mantain the order of appearence


def describe_pet(animal_type, pet_name):
    print(f'my pet {pet_name} is green')
    print(f"my pet is a {animal_type} and it's name is {pet_name}")


describe_pet(pet_name='bubu', animal_type='snake')

# Default values are arguments passed within the function (as KW arguments) and that are ignored if the function is invoked with a different value

def describe_pet(animal_type, pet_name='pichicho'):
    print(f'my pet {pet_name} is green')
    print(f"my pet is a {animal_type} and it's name is {pet_name}")


describe_pet(animal_type='snake')
print(type(describe_pet))

# Making arguments optional


def format_name(first_name, last_name, mid_name=''):
    if mid_name:
        full_name = f'{first_name} {mid_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()


person = format_name('jimmi', 'curtis', mid_name='lee')
# person = format_name('jimmi', 'carter')


print(person)


# return Dictionary from function


def build_person(first_name, last_name, age=None):
    person = {
        'first': first_name,
        'last': last_name
        }
    if age:
        person['age'] = age
    return person

print(build_person('manolo', 'gomez', 23))


# Using loop w/function

#passing a list 
def greeter(names):
    for name in names:
        print(f"hola {name.title()}")

personas = ['sofi', 'richard', 'cande']
greeter(personas)


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("Please enter your name")
    f_name = input('first name: ')
    if f_name =='q':
        break
    l_name = input('last name: ')
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f'hola {formatted_name}')


#passing and completing lists w/functions
#non-function version

while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f'printing {current_design}')
    completed_models.append(current_design)

print('the following models have been printed')
for completed_model in completed_models:
    print(completed_model)


#2 functions version
def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'printing {current_design}')
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print('all models have been printed')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['d1', 'd1', 'd3', 'd4', 'd5']
completed_models = []


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

""" 

#usando la funcion de importar modulo

import pizza
pizza.make_pizza(12,'kesito')

# traer solo x funcion desde modulo

import pizza as mp
mp.make_pizza(13,'peperoni')

from pizza import make_pizza as mp
mp(19,'extra kesito')


