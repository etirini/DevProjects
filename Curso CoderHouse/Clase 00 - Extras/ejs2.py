#Clase Empleado: Prop: Nombre, Apllido, Cia, Email (nomber + apellido + @ + Cia + .com)
#Clase Rrhh: funciones para contratar y echar
#Subclase Developer(Empleado): prog_lan
#Subclase Manager(Empleado, Rrhh): estilo_mgmt, equipo=[], usa las funciones de Rrhh




class Empleado:
    def __init__(self, nombre, apellido, legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
    
class Manager(Empleado):
    def __init__(self, nombre, apellido, legajo, area):
        super().__init__(nombre, apellido, legajo)
        self.area = area
       
class Developer(Empleado):
    def __init__(self, nombre, apellido, legajo, lenguaje):
        super().__init__(nombre, apellido, legajo)
        self.lenguaje = lenguaje

mgr1 = Manager("Esteban", "Tirini", 123, "Marketing")
dev1 = Developer("Juan Carlos", "Milanesa", 230, "Python")

#print(mgr1.nombre, mgr1.apellido, mgr1.area, mgr1.legajo, mgr1.area)
#print(dev1.nombre, dev1.apellido, dev1.legajo, dev1.lenguaje)
