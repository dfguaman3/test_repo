import unittest
import math
class Persona:

    def __init__(self,Nombre,Apellido,edad,lista_out,factor,salida):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.edad = edad
        self.lista_out=lista_out
        self.fator=factor
        self.salida=salida
    @property
    def fullname(self):
        return f'{self.Nombre.capitalize()} {self.Apellido.capitalize()}'
    @property
    def date(self):
        if type(self.edad) != int(self.edad) and self.edad < 1:
            raise TypeError('Ingrese un año valido')
        self.edad=2021-self.edad
        return self.edad
    
    def mean_list(self,lista):
        suma = 0
        for i in lista:
            suma += i
            self.lista_out = suma / len(lista)
        return self.lista_out
    def fact(self, numero):
        self.factor = math.factorial(numero)
        return self.factor
    def modulo(self,numero2):
        if numero2%2==0:
            self.salida="par"
            print(self.salida)
        else:
            self.salida="impar"
            print(self.salida)
        return self.salida
if __name__ == '__nmain__':
    unittest.main()
