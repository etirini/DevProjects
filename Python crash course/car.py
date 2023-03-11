
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # podemos pasar un atributo con un valor default sin agregarlo a los parametros de la clase
        self.odometer = 0

    def get_description(self):
        print(
            f'Este auto es un {self.make} modelo {self.model} del anio {self.year}')

    def read_odometer(self):
        print(f'Este auto lleva recorridos {self.odometer} kilometros')

    # modificar un atributo mediante un metodo
    def update_odometer(self, kms):
        # agregando una comprobacion de los datos
        if kms >= self.odometer:
            self.odometer = kms
            print(
                f'Se actualizo el valor de odometer a {self.odometer} kilometros')
        else:
            print(
                f'No se puede cargar un valor menor al existente, actualmente {self.odometer} kilometros.')

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


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery(battery_size=99)

    def fill_tank(self, lts):
        print('This is an electric car. Do not use gas')


class Battery:
    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'The battery size is {self.battery_size}')

    def get_range(self):
        if self.battery_size <= 75:
            self.range = 250
        elif self.battery_size > 75:
            self.range = 400
        print(f'La bateria tiene una autonomia de {self.range} kilometros')
