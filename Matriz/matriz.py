#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:49:50 2021

@author: ariel
"""
import random
def matriz_random():
    """
    Genera una matriz de 5x5 con numeros aleatoreos
    """
    matriz = [[int(random.random()*10) for j in range(5)] for i in range(5)]
    return matriz
def buscar_consecutivos(matriz):
    """
    recorre la matriz y busca si hay numeros consecutivos 
    horizontal o verticalmente
    """
    for i in range(5):       
        for j in range(5):
            if j < 2:
                 inicial = matriz[i][j]
                 if matriz[i][j+1]-1 == inicial and matriz[i][j+2]-2 == inicial and matriz[i][j+3]-3 == inicial:
                     print(f'(Horizontal)Numeros consecutivos entre [{i}][{j}] y [{i}][{j+3}] : {matriz[i][j]}, {matriz[i][j+3]}')
        if i < 2:
            inicial1 = matriz[i][j]
            if matriz[i+1][j]-1 == inicial1 and matriz[i+2][j]-2 == inicial1 and matriz[i+3][j]-3 == inicial1:
                print(f'(Vertical)Numeros consecutivos entre [{i}][{j}] y [{i+3}][{j}] : {matriz[i][j]}, {matriz[i+3][j]}')

for i in range(10000):
    matriz = matriz_random()
    buscar_consecutivos(matriz)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
