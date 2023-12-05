import numpy as np
from math import *
from tabulate import tabulate
# вариант номер 13 (1)

# функция подсчета нормы
def func_norm(matrix):
    s=[]
    for j in range(25):
        s.append(sum([abs(matrix[i][j]) for i in range(25)]))
    return max(s)

# функция подсчета числа обусловленности
def func_cond(matrix):
    matrix_obr=np.linalg.inv(matrix)
    return(func_norm(matrix) * func_norm(matrix_obr))

# функция подсчета векторной нормы (как суммы)
def func_norm_vector(x):
    return(sum([abs(x[i]) for i in range(25)]))

A=np.random.rand (25, 25)
B=np.random.rand (25, 25)
C=np.random.rand (25, 25)
D=np.random.rand (25, 25)
E=np.random.rand (25, 25)
# print("Матрица А: ", A)
# print("Матрица В: ", B)
# print("Матрица С: ", C)
# print("Матрица D: ", D)
# print("Матрица D: ", E)

table=[('1', func_norm(A), func_cond(A)),
       ('2', func_norm(B), func_cond(B)),
       ('3', func_norm(C), func_cond(C)),
       ('4', func_norm(D), func_cond(D)),
       ('5', func_norm(E), func_cond(E))]

names=['Номер', 'Норма матрицы', 'Число обусловленности матрицы']
print(tabulate(table, headers=names, tablefmt="heavy_grid"))

x=np.linspace(0, 1, num=25)
V=np.vander(x, increasing=True)
a_tochn=np.ones((25, 1))
y= V @ a_tochn
# соответственно a_tochn это точное решение данной системы
a=np.linalg.solve(V, y)
# print(a)

print("Число обусловленности матрицы Волан-де-Морта (Вандермонда): ", func_cond(V))

# векторная норма как максимум
# print("Норма вектора точного решения: ", 1.0)
# print("Норма вектора приближенного решения: ", max([abs(x[i]) for i in range(25)]))

# векторная норма как сумма
print("Норма вектора точного решения: ", func_norm_vector(a_tochn))
print("Норма вектора приближенного решения: ", func_norm_vector(a))

print("Абсолютная погрешность: ", func_norm_vector(a_tochn-a))
print("Относительная погрешность: ", func_norm_vector(a_tochn-a)/func_norm_vector(a_tochn))
