#Write a recursive function to count items in list

def cuentArray(arr):
    if arr == []:
        return 0
    #Uno de los dos return tiene que estar siempre comentado.
    return 1 + cuentArray(arr[1:])
    #en este la funcion devuelve la cantidad de elementos que hay en el array
    #return arr[0] + cuentArray(arr[1:])
    #en este la funcion devuelve la suma de los valores que se encuentran en el array

print(str(cuentArray([1,2,3])))




