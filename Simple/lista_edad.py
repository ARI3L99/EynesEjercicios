#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:14:20 2021

@author: ariel
"""
import random
def lista_dic():
    """
    Crea una lista con 10 diccionarios con id randoms entre 1 y 100
    """
    lista = [{"edad":random.randint(1, 100)} for i in range(10)]
    return lista

def ordenar(lista):
    """
    ordena la lista e imprime por pantalla el mayor y el menor
    """
    lista_ord = sorted(lista, key=lambda k: k["edad"])
    print(f"Número mayor : {max(lista, key= lambda k : k['edad'])['edad']} ")
    print(f"Número menor : {min(lista, key= lambda k : k['edad'])['edad']} ")
    return lista_ord
lista = lista_dic()
print(lista)
lista_ordenada = ordenar(lista)
print(lista_ordenada)
if __name__ == "__main__":
    import doctest
    doctest.testmod()