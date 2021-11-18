#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 12:47:22 2021

@author: ariel
"""
"""
Escribir una clase en python llamada círculo que contenga un radio, con un método que
devuelva el área y otro que devuelva el perímetro del círculo.
Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
usuario e impidiendo la instanciación.
Si printeamos el objeto creado debe mostrarse una representación amigable.
El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
mostrar un error y no permitir modificación.
Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
multiplicado por n. No permitir la multiplicación por números <= 0
"""
import math
class Circulo:
    def __init__(self,radio):
        if radio <= 0:
            raise ValueError("Solo puede usar numeros mayores a 0")
        self.radio = radio
       
    def area(self):
        return (math.pi * self.radio**2)
    
    def perimetro(self):
        return (2 * math.pi * self.radio)
    
    def __str__(self):
        return f'Radio del circulo = {self.radio} Area = {self.area():.2f} Perimetro = {self.perimetro():.2f}'
   
    def __repr__(self):
        return f"Radio circulo = {self.radio} Area = {self.area():.2f} Perimetro = {self.perimetro():.2f}"
    
    def __mul__(self,n):
        return Circulo(self.radio * n)

    def __setattr__(self, name, value):
        if not value <= 0:
            return super().__setattr__(name, value)

c = Circulo(3)
print("C = ",c)
c.radio = 0 #No se modifica
print("c.radio = 0")
c1 = Circulo(5)
print("C1 =" ,c1)
c1.radio = 10 #Si se modifica
print("c1.radio = 10")
print("C =", c,"\n","C1",c1)
print("c*0")
print(c*0)
if __name__ == "__main__":
    import doctest
    doctest.testmod()