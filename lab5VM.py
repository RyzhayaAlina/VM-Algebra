import numpy as np
from math import *

# Метод Зейделя (вариант 13)

def func_sum_elements(A, n):
    sum1=0
    for i in range(n):
        for j in range(n):
            if i!=j:
                sum1+=abs(A[i, j])
    return(sum1)

def func_convergence(A, n):
    flag = True
    for i in range(n):
        if abs(A[i, i])>func_sum_elements(A, n):
            flag = True
        else:
            flag = False
    if flag==True: return("Метод Зейделя для данной матрицы сходится")
    else: return("Метод Зейделя для данной матрицы не сходится")

def func_error_rate(x, x_new, n):
    return(sum([abs(x_new[i] - x[i])  for i in range(n)]))

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

n = 4
# # система №1
# A = np.array([[10, 2, 1],
#             [1, 10, 2],
#             [1, 1, 10]])
# b = np.array([[10], [12], [8]])

# A = np.array([[4, -1, -6, 0],
#             [-5, -4, 10, 8],
#             [0, 9, 4, -2],
#             [1, 0, -7, 5]])
# b = np.array([[2], [21], [-12], [-6]])
# x_tochn = np.linalg.solve(A, b)

A = np.array([[6.22, 1.42, -1.72, 1.91],
            [1.42, 5.33, 1.11, -1.82],
            [-1.72, 1.11, 5.24, 1.42],
            [1.91, -1.82, 1.42, 6.55]])
b = np.array([[7.53], [6.06], [8.05], [8.06]])
x_tochn = np.linalg.solve(A, b)

# система №2
# A = np.array([[10, -1, 1],
#             [1, 10, -3],
#             [1, -2, 10]])
# b = np.array([[10], [8], [9]])
# x_tochn = np.linalg.solve(A, b)

# проверка матрицы на сходимость
print(func_convergence(A, n))

A_ya = get_coff_A(A, n)
b_ya = get_coff_b(A, b, n)


k = 0
e = 10**(-4)
w = 1
x = np.zeros((n, 1))
error_rate = 1
while error_rate > e:
    x_new = np.copy(x)
    for i in range(n):
        x_new[i] = sum(A_ya[i, j]*x[j] for j in range(i, n)) + sum(A_ya[i, j]*x_new[j] for j in range(0, i)) + b_ya[i]
        # x_new[i] = (1+w)*x[i]+ w*(sum(A_ya[i, j]*x[j] for j in range(i, n)) + sum(A_ya[i, j]*x_new[j] for j in range(0, i)) + b_ya[i])
    error_rate = func_error_rate(x, x_new, n)
    k+=1
    x=x_new

print("Количество итераций: ")
print(k)
print("Точное решение Слау: ")
print(x_tochn)
print("Решение Слау методом Зейделя: ")
print(x)
