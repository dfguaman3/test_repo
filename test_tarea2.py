import unittest
from tarea2 import Persona

class TestPersona (unittest.TestCase):
    try:
        def setUp(self):
            self.datos = Persona('Daniel','Guaman',1990,5,720,"par")#Nombre,Apellido,año_nacimiento,promediolista,factorial,modulo
        print('Setting up1')
        def tearDown(self):
            print('Setting up2')
        def test_fullname(self):
            self.assertEqual(self.datos.fullname,'Daniel Guaman')
        def test_date(self):
            self.assertEqual(self.datos.date, 31)
        def test_mean_list(self):
            self.assertEqual(self.datos.mean_list([1,3,5,7,9]),5)
        def test_numfact(self):
            self.assertEqual(self.datos.fact(6),720)
        def test_modulo(self):
            self.assertEqual(self.datos.modulo(10),"par")

    except Exception as e:
        print(e)

if __name__ == '__main__':
    unittest.main()