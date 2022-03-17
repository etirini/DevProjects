# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2
# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining(elapsed_bake_time):
    return EXPECTED_BAKE_TIME - elapsed_bake_time


    pass

# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here
def preparation_time_in_minutes(number_of_layers):
   return PREPARATION_TIME * number_of_layers

# TODO: define the 'elapsed_time_in_minutes()' function

def elapsed_time_in_minutes(preparation_time_in_minutes, bake_time_remaining):
    return  preparation_time_in_minutes + bake_time_remaining


print(elapsed_time_in_minutes(preparation_time_in_minutes(1), bake_time_remaining(10)))
