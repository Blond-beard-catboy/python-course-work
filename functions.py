import matplotlib.pyplot as plt
import numpy as np
import math
from random import randint

#параметры матрицы через input() !!!!
A = []
N = 3
M = 2

#Функция создает нулевую матрицу размера N x M
def makeNullMatrix(N: int, M: int)-> None:
    for i in range(N):
        A.append([0]*M)
    print(A)

#Функция вставляет случайные значения от 1 до 10 включительно
def insertValue(A: list[list], N: int, M: int)-> None:
    for i in range(N):
        for j in range(M):
            A[i][j] = randint(1, 10)
    print(A)

#Табличный вывод матрицы по ее индексам
def tableSight(A: list[list])-> None:
    for i in range(len(A)):         
        print(A[i], end = ' ')
        print()                 




#Функция возвращает транспонированную матрицу
def transposeMatrix(matrix: list[list]) -> list[list]:
    transposed_matrix = [[0 for i in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


if __name__ == "__main__":
    makeNullMatrix(N, M)
    insertValue(A, N, M)
    print(A)
    print()
    tableSight(transposeMatrix(A))
