import numpy as np
from math import *

# Метод Ричардсона (вариант 13)

def get_coff_A(A, n):
    A_ya = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i==j:
                A_ya[i, j] = 0
            else:
                A_ya[i, j] = - A[i, j]/A[i, i]
    return(A_ya)

def get_coff_b(A, b, n):
    b_ya = np.zeros((n, 1))
    for i in range(n):
        b_ya[i] = b[i]/A[i, i]
    return(b_ya)

def func_error_rate(x, x_new, n):
    return(sum([abs(x_new[i] - x[i])  for i in range(n)]))

n=4
# система №1
A = np.array([[4, -1, -6, 0],
            [-5, -4, 10, 8],
            [0, 9, 4, -2],
            [1, 0, -7, 5]])
b = np.array([[2], [21], [-12], [-6]])
x_tochn = np.linalg.solve(A, b)

# система №2
# A = np.array([[6.22, 1.42, -1.72, 1.91],
#             [1.42, 5.33, 1.11, -1.82],
#             [-1.72, 1.11, 5.24, 1.42],
#             [1.91, -1.82, 1.42, 6.55]])
# b = np.array([[7.53], [6.06], [8.05], [8.06]])
# x_tochn = np.linalg.solve(A, b)

L=np.linalg.eigvals(A)

A_ya = get_coff_A(A, n)
b_ya = get_coff_b(A, b, n)

t0=2/(max(L)+min(L))
ny=min(L)/max(L)
p0=(1-ny)/(1+ny)

x = np.zeros((n, 1))
e = 10**(-4)
N = 6   # количество шагов
for k in range(N):
    x_new = np.copy(x)
    V=np.cos(((2*(k+1) - 1)*pi)/(2*N))
    t_new = t0/(1+p0*V)
    x_new = x + t_new*(A_ya @ x + b_ya)
    error_rate = func_error_rate(x, x_new, n)
    x=x_new
    if error_rate > e: print("Шаг номер:", k)
    else: print("Не этот шаг:", k)

print("Точное решение Слау: ")
print(x_tochn)
print("Решение Слау методом Ричардсона: ")
print(x)
