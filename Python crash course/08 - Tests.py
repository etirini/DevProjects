#seteando un entorno en el que vamos a probar una funcion

#primero creamos la funcion, esta toma un nombre y un apellido y los devuelve formateados
#la funcion que necesitamos se encuentra en name_function.py y se llama get_formatted_name
#para realizar la prueba invocamos el modulo de test unit y creamos una clase con un nombre relacionado al test que vamos a hacer

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
    #verificamos si un nombre con first y last eqiuvale a una string formateado como First Last
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        formated_name = get_formatted_name('kurt', 'cobain', 'donald' )
        self.assertEqual(formated_name,'Kurt Donald Cobain')

if __name__ == '__main__':
    unittest.main()

