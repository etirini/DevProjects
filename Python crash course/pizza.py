
"""
#the notation below can be used to pass a copy of the list to avoid permanent changes on a list (or losing it completely)

# example_list = [1,2,3,4,5]
# def function(example_list[:]) 

#passing n amount of arguments to a function. *is used before the argument(s) in the function call

"""

def make_pizza(size, *toppings):
    print(f'preparing {size} inch pizza with toppings ')
    for topping in toppings:
        print(f'adding {topping}')
