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

class Developer(Empleado):
    def __init__(self, nombre, apellido, cia, sueldo, prog_lang): #Developer
        super().__init__(nombre, apellido, cia, sueldo ) #Trae de empleado
        self.prog_lang = prog_lang
        self.aumento = 1.10

    def dar_aumento(self):
        self.sueldo = (self.sueldo * self.aumento)
        print(self.sueldo)

class Manager(Empleado):
    def __init__(self, nombre, apellido, cia, sueldo, estilo_mgmt, empleados=None):
        super().__init__(nombre, apellido, cia, sueldo)
        self.estilo_mgmt = estilo_mgmt
        if self.empleados is None:
            self.empleados = []
        else:
            self.empleados = empleados
        


#empleado1 = Empleado('Juan', 'Gomez', 'tuvieja')
#print(empleado1.nombre, empleado1.apellido, empleado1.cia, empleado1.email)

dev1 = Developer('Juan', 'Gomez', 'tuvieja', 5000 ,'python')
print(dev1.nombre, dev1.apellido, dev1.cia, dev1.email, dev1.sueldo, dev1.prog_lang )

dev1.dar_aumento()
print(dev1.nombre, dev1.apellido, dev1.cia,
      dev1.email, dev1.sueldo, dev1.prog_lang)



