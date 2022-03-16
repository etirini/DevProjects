primera_nota = int(input("Indicar primera nota "))
segunda_nota = int(input("Indicar segunda nota "))
#Es un poco contradictorio que el el ppt dice que los valores tienen que pedirse mediante input pero despues dice que los valores de ponderacion son fijos. 
#Prefiero pasar todo como variable :-) 
ponderacion_primera_nota = int(input("Indicar la ponderacion de la primera nota "))
ponderacion_segunda_nota = int(input("Indicar la ponderacion de la segunda nota "))

promedio = (primera_nota + segunda_nota) /2
print("El promedio es " + str(promedio))

promedio_ponderado = (primera_nota * ponderacion_primera_nota + segunda_nota * ponderacion_segunda_nota) / (ponderacion_primera_nota + ponderacion_segunda_nota)
print(f"El promedio ponderado es {promedio_ponderado}")
