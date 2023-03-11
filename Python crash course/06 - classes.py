class Dog:
#inicializar la clase
    def __init__(self, name, age):
#definir atributos de clase (name, age)
        self.name = name
        self.age = age

    def sit(self):
#definimos una accion (metodo)(sit):
        print(f'{self.name} is now sitting')

    def roll(self):
#definimos una accion (metodo)(roll):
        print(f'{self.name} is now rolling over')


#my_dog = Dog('chuchu', 2)
#print(my_dog.name)
#my_dog.sit()
class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'The battery size is {self.battery_size}')

    def get_range(self):
        if self.battery_size <= 75:
            self.range = 250
        elif self.battery_size >75:
            self.range = 400
        print(f'La bateria tiene una autonomia de {self.range} kilometros')


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        #podemos pasar un atributo con un valor default sin agregarlo a los parametros de la clase
        self.odometer = 0

    def get_description(self):
        print(f'Este auto es un {self.make} modelo {self.model} del anio {self.year}')
    
    def read_odometer(self):
        print(f'Este auto lleva recorridos {self.odometer} kilometros')

    #modificar un atributo mediante un metodo
    def update_odometer(self, kms):
        #agregando una comprobacion de los datos
        if kms >= self.odometer:
            self.odometer = kms
            print(f'Se actualizo el valor de odometer a {self.odometer} kilometros')
        else:
            print(f'No se puede cargar un valor menor al existente, actualmente {self.odometer} kilometros.')

    def increment_odometer(self, kms):
        if kms > 0:
            self.kms = kms
            self.odometer += kms
            print(f'se incremento el odometer en {self.kms} kilometros')
            print(f'el valor de odometer es {self.odometer} kilometros')
        else:
            print('No se puede actualizar por un valor negativo o cero')

    def fill_tank(self, lts):
        self.lts = lts
        max_lts = 120
        if self.lts > max_lts:
            print(f'cannot fill tank with more than {max_lts}') 
        else:
            print(f'Filling tank with {self.lts}')

#my_car = Car('Audi', 'TT Roadster', 2002 )
#my_car_longname = Car.get_description(my_car)
#my_car.read_odometer()

#Para modificar el valor de un atributo se puede modificar directamente mediante una instancia, modificar mediante un metodo o incrementar mediante un metodo

#modificar directamente via instancia
#my_car_2 = Car('bmw', 'x4', 2020)
#my_car_2.odometer = 45

#my_car_2.get_description()
#my_car_2.read_odometer()

#modificar mediante un metodo. ejemplo llamando instancia:
#my_car_3 = Car('Ford', 'Fiesta', 2001)

#comprobando que el metodo de comprobacion de los datos de kms/odometer funcione
#my_car_3.read_odometer()
#my_car_3.update_odometer(30)

#comprobando el incremento de odometer
#my_car_3.increment_odometer(120)
#my_car_3.increment_odometer(0)

#Inheritance de clases

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(battery_size=99)

    def fill_tank(self, lts):
        print('This is an electric car. Do not use gas')


my_car_4 = ElectricCar('tesla', 's', 2020)
my_car_4.get_description()
my_car_4.battery.describe_battery()
my_car_4.battery.get_range()

#my_car_2.fill_tank(110)
#my_car_4.fill_tank(10)

