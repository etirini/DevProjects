voted = {}

def checkvote(name):
    if voted.get(name):
        print("Already voted")
    else: 
        voted[name] = True #True viene a ser el valor alojado en el index al que hace referencia name. En el ejemplo del libro, true
        #es el precio de la manzana. Supongo que lo hace asi para no meter valores tipo int o string cuando no los necesita.
        print("Let them vote")

checkvote("Esteban")
checkvote("Juan")
checkvote("Maria")
checkvote("Esteban")
print(voted)