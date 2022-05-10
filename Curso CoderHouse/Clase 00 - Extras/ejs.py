#Empleado: Prop: Nombre, Apllido, Cia, Email (nomber + apellido + @ + Cia + .com)
#Subclase Developer(Empleado): prog_lan, dar_aumento 10%
#Subclase Manager(Empleado): estilo_mgmt, empleados=[], contratar_dev(Developer) *Suma developer a lista developers, echar_dev, listar_dev *dunder __str__



class Empleado:
    def __init__(self, nombre, apellido, cia, sueldo):
        self.nombre = nombre 
        self.apellido = apellido
        self.cia = cia
        self.email = self.nombre + self.apellido + '@' + cia + '.com'
        self.sueldo = sueldo

    def fullname(self):
        return '{} {}'.format(self.nombre, self.apellido)

class Developer(Empleado):
    def __init__(self, nombre, apellido, cia, sueldo, prog_lang): #Developer
        super().__init__(nombre, apellido, cia, sueldo ) #Trae de empleado
        self.prog_lang = prog_lang
        self.aumento = 1.10

    def dar_aumento(self):
        self.sueldo = (self.sueldo * self.aumento)
        print(self.sueldo)

class Manager(Empleado):
    def __init__(self, nombre, apellido, cia, sueldo, estilo_mgmt, a_cargo=None):
        super().__init__(nombre, apellido, cia, sueldo)
        self.estilo_mgmt = estilo_mgmt
       
        if self.a_cargo is None:
            self.a_cargo = []
        else:
            self.a_cargo = a_cargo

    def add_acargo(self, emp):
        if emp not in self.a_cargo:
            self.a_cargo.append(emp)



#empleado1 = Empleado('Juan', 'Gomez', 'tuvieja')
#print(empleado1.nombre, empleado1.apellido, empleado1.cia, empleado1.email)

dev1 = Developer('Juan', 'Gomez', 'tuvieja', 5000 ,'python')
mgr1 = Manager('Esteban', 'Tirini', "PHM", 85000, 'Service Management',['aaaa'])

