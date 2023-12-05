import numpy as np
from math import *

n=3
# тест
# A = np.array([[6.03, 13, -17],
#             [13, 29.03, -38],
#             [-17, -38, 50.03]])
# b = np.array([[2.0909], [4.1509], [-5.1191]])
# x_tochn = np.array([[1.03], [1.03], [1.03]])

# система из лабораторной работы
A = np.array([[2, 0, 1],
            [0, 1, -1],
            [1, -1, 1]])
b = np.array([[3], [0], [3]])
x_tochn =  np.linalg.solve(A, b)

Q = np.zeros((n,n))
U = np.zeros((n,n))

for i in range(n):
    if i==0:
        U[::, i] = A[::, i]
    else:
        U[::, i] = A[::, i]-(sum([np.dot(A[::, i], Q[::, j]) * Q[::, j] for j in range(i)]))
    Q[::, i] = U[::, i]/np.linalg.norm(U[::, i])

print("Ортогональная матрица Q: ")
print(Q)

R = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        if j>=i:
            R[i][j] = np.dot(A[::, j], Q[::, i])

print("Матрица перехода R: ")
print(R)

print("Проверка, исходная матрица А: ")
print(A)
print("Проверка, матрица А как перемножение Q и R: ")
print(Q @ R)

y = np.transpose(Q) @ b
x = np.linalg.solve(R, y)

print("Точное решение: ")
print(x_tochn)
print("Приближенное решение: ")
print(x)