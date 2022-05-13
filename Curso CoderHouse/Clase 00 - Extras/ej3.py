#import datetime

class Employee:
    raise_amnt = 1.04


    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@compania.com'
        #Employee.num_of_employees += 1 #Demo de uso de una variable sin self. La idea es que aumenta por cada empleado que existe

    """ def fullname(self): Comento esta linea porque reemplace la funcion de fullname por su version con decorator
        return '{} {}'.format(self.first, self.last) """
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property #Definimos email como una funcion (metodo) en la clase pero la podemos acceder como un atributo (propiedad)
    def email(self):
        return '{}.{}@compania.com'.format(self.first, self.last)

    @fullname
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amnt)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    def __add__(self, other): #prueba de dunders
        return self.pay + other.pay

    def __len__(self):  # prueba de dunders
        return len(self.fullname())
"""
    #Metodos regulares toman la instancia sobre la que corre el metodo mediante (self). si quisiera tomar la clase en vez del la instancia se usar el class decorator 
    # @classmethod
    def set_raise_amnt(cls, amount):
        cls.raise_amnt = amount

    @staticmethod #metodos que no tienen relacion de codigo con la clase pero que seria logico asociar para mantener un order. No reciben self o cls como argumento por no
    #estar asociado medinte codigo a la clase o instancia
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True

my_date = datetime.date(2016, 7, 11)
print(Employee.num_of_employees)
print(Employee.raise_amnt)
print(Employee.is_workday(my_date))

"""
class Developer(Employee):
    raise_amnt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
            return print('Se agrego al empleado')
        else:
            return print("El empleado {} ya se encuentra en la lista".format(Employee.fullname(emp)))

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
            return print('Se elimino al empleado')
        else:
            return print("El empleado {} ya no se encuentra en la lista".format(Employee.fullname(emp)))
    
    def pnt_emp(self):
        for emp in self.employees:
            print(emp.fullname())

emp1 = Employee('Pocho', 'Lapantera', 5000)
emp2 = Employee('Cuchu', 'Nose', 5000)
mgr1 = Manager("Esteban", "Tirini", 5000, [])
#print(emp1.raise_amnt)

""" 
************ PRUEBAS DE AGREGAR, LISTAR, REMOVER ************
mgr1.add_emp(emp1)
mgr1.add_emp(emp1)
mgr1.pnt_emp()
mgr1.add_emp(emp2)
mgr1.rem_emp(emp1)
mgr1.pnt_emp()
repr(emp1) 
"""

""" 
************ PRUEBAS DE DUNDERS STR, REPR, ADD************
print(repr(emp1)) #representacion de como los datos son ingresador. El output del repr debe mostrarse como se ingresarian los datos en esa clase.
print(str(emp1)) #representacion para el usuario de los datos de un elemento en una clase. 
print(emp1 + emp2) #prueba dunder add 
print(len(emp1)) #prueba dunder len
"""

emp1.fullname = 'Empleado Uno'
