from random import randint as RI
from random import choice as CH 
""" 
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        #print(f'this restaurant is called {self.restaurant_name} and specialices in {self.cuisine_type} food and has served {self.served_clients} clients')
        #Tuve que eliminar el describe de arriba porque abarca demasiado (hacer q describa la cantidad de servidos lo hace complejo para IceCreamStand)
        print(f'this restaurant is called {self.restaurant_name} and specialices in {self.cuisine_type} food')

    def tables_served(self, served_clients):
        self.served_clients = served_clients

#resto1 = Restaurant('cucu', 'asiatica')
#En la linea de abajo estoy modificando el atributo directamente en vez de usar un metodo (como en la linea de mas abajo)
#resto1.served_clients = 12
#resto1.tables_served(25)
#resto1.describe_restaurant() 

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='postres'):
        super().__init__(restaurant_name, cuisine_type)
        
        self.flavours = ['choco', 'vainilla', 'frutilla', 'anana']
    
    def get_flavours(self):
        print(f'{self.flavours}')

mi_resto = IceCreamStand('la crema de tu vieja')
mi_resto.describe_restaurant()


class User():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
    def get_b_data(self,day, month, year):
        self.b_day = day
        self.b_month = month
        self.b_year = year

    def describe_user(self):
        print(f'{self.first_name} {self.last_name} nacio el {self.b_day} de {self.b_month} de {self.b_year}')
        
#user1 = User('fulano', 'martinez')
#user1.get_b_data(12,11,1986)
#user1.describe_user()

class Dice():
    def __init__(self, sides=6):
        self.times_rolled = 0
        self.sides = sides
    
    def roll_dice(self):
        while self.times_rolled < 10:
            self.roll = RI(1, self.sides)
            print(f'El dado dice {self.roll}')
            self.times_rolled +=1
        print('Se terminaron los intentos')

my_roll = Dice(200)
my_roll.roll_dice()
"""

possibilities = [99, 30, 15, 'E', 20, 12, 4, 7, 'F']
my_ticket = [99, 30, 15, 'E']
ticket_counter = 0
won = False

def random_ticket_generator(possibilities):
    played_ticket = []
    while len(played_ticket) < 4:
        picked_element = CH(possibilities)
        if picked_element not in played_ticket:
            played_ticket.append(picked_element)
    print(played_ticket)
    return played_ticket

def compare_tickets(played_ticket, my_ticket):
    for element in played_ticket:
        while element not in my_ticket:
            return False
    return True

while not won:
    ticket = random_ticket_generator(possibilities)
    won = compare_tickets(ticket, my_ticket)
    ticket_counter = ticket_counter + 1

if won:
    print(f'ganaste despues de {ticket_counter} intentos')

