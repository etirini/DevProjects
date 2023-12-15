usr_name = input("Introduzca su nombre ")
print(f"hola,",usr_name)

try:
    usr_hours = input("Introduzca cantidadd de horas a facturar ")
    usr_hours = float(usr_hours)
except:
    print("horas no validas")
try:
    usr_rate = input("Introduzca rate ")
    usr_rate = float(usr_rate)
except:
    print("Rate no valido")

usr_payment = usr_hours * usr_rate
print(f"Se debe pagar",usr_payment)

