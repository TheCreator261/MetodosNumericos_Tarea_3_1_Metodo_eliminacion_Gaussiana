# -*- coding: utf-8 -*-
"""Tarea 3.1 Metodo de Eliminacion Gaussiana.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HFrKlppkPFt5DIsTgQIK-8OwnYCFyIP1
"""

#Antonio Josue Rodriguez Falcon
#Ejercicio 1

import numpy as np

def gauss_elimination(A, b):
    A = A.copy()
    b = b.copy()
    n = len(b)

    for i in range(n):

        max_row = i + np.argmax(np.abs(A[i:, i]))
        if max_row != i:
            A[[i, max_row], :] = A[[max_row, i], :].copy()
            b[[i, max_row]] = b[[max_row, i]].copy()


        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]


    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


A = np.array([
    [3, 2, -1, 4],
    [5, -3, 2, -1],
    [-1, 4, -2, 3],
    [2, -1, 3, 5]
], dtype=float)

b = np.array([10, 5, -3, 8], dtype=float)


sol = gauss_elimination(A, b)

print("Solución del sistema:")
print(sol)

#Antonio Josue Rodriguez Falcon
#Ejercicio 2

import numpy as np

def gauss_elimination(A, b):
    A = A.copy()
    b = b.copy()
    n = len(b)

    for i in range(n):

        max_row = i + np.argmax(np.abs(A[i:, i]))
        if max_row != i:
            A[[i, max_row], :] = A[[max_row, i], :].copy()
            b[[i, max_row]] = b[[max_row, i]].copy()


        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]


    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


A = np.array([
    [6, -2, 3, -1, 2],
    [-3, 5, -2, 4, -1],
    [4, 3, 7, -5, 3,],
    [-2, 6, -3, 1, -4],
    [1, -3, 2, -5, 6]
], dtype=float)

b = np.array([15, -6, 20, -4, 7], dtype=float)


sol = gauss_elimination(A, b)

print("Solución del sistema:")
print(sol)

#Antonio Josue Rodriguez Falcon
#Ejercicio 3

import numpy as np

def gauss_elimination(A, b):
    A = A.copy()
    b = b.copy()
    n = len(b)

    for i in range(n):

        max_row = i + np.argmax(np.abs(A[i:, i]))
        if max_row != i:
            A[[i, max_row], :] = A[[max_row, i], :].copy()
            b[[i, max_row]] = b[[max_row, i]].copy()


        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            b[j] -= factor * b[i]


    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


A = np.array([
    [1, 2, -3, 4, -1, 1],
    [-2, 3, 5, -1, 2, -1],
    [4, -1, 2, 6, -3, 1],
    [-3, 5, -1, 2, 4, -1],
    [2, -4, 6, -5, 1, 3],
    [-5, 1, 4, -1, 2, -6]
], dtype=float)

b = np.array([7, -2, 10, 3, -8, 5], dtype=float)


sol = gauss_elimination(A, b)

print("Solución del sistema:")
print(sol)