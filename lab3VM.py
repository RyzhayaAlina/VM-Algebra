import numpy as np
from math import *
# вариант 13 (т.е. 3)

n=3
# тест
# A=np.array([[81, -45, 45],
#             [-45, 50, -15],
#             [45, -15, 38]])
# b=np.array([[531], [-460], [193]])
# x_tochn=np.array([[6], [-5], [-4]])

# СЛАУ 1
# A=np.array([[5.8, 0.3, -0.2],
#             [0.3, 4.0, -0.7],
#             [-0.2, -0.7, 6.7]])
# b=np.array([[3.1], [-1.7], [1.1]])
# x_tochn=np.linalg.solve(A, b)

# СЛАУ 2
A=np.array([[4.12, 0.42, 1.34, 0.88],
            [0.42, 3.95, 1.87, 0.43],
            [1.34, 1.87, 3.20, 0.31],
            [0.88, 0.43, 0.31, 5.17]])
b=np.array([[11.17], [0.115], [9.909], [9.349]])
x_tochn=np.linalg.solve(A, b)
n+=1

# print(np.linalg.eigvals(A))

# Проверка входной матрицы на условия
if np.all(A==np.transpose(A)):
    if np.all(np.linalg.eigvals(A) > 0):
        print("Матрица А симметричная и положительно определенная")
    else:
        print("Матрица не определена положительно ")
else:
    print("Матрица не симметричная")

U=np.zeros((n,n))
U[0, 0]=np.sqrt(A[0, 0])

# заполнение матриц
for j in range(1, n):
    U[0, j]=A[0, j]/U[0, 0]

for i in range(1, n):
    for j in range(1, n):
        if i==j:
            U[i, i]=np.sqrt(A[i, i]-sum([U[k, i]* U[k, i] for k in range(i)]))
        if i<j:
            U[i, j]=(A[i, j]-sum([U[k, i]* U[k, j] for k in range(i)]))/U[i, i]

U_trans=np.transpose(U)
print("Матрица U: ")
print(U)
print("Матрица U транспонированная: ")
print(U_trans)

# Проверка
print("Произведение: ")
print(U_trans @ U )
print("Ориганальная А: ")
print(A)


# # получение решения
y = np.linalg.solve(U_trans, b)
x_solve = np.linalg.solve(U, y)
print("Приблеженное решение: ")
print(x_solve)
print("Точное решение: ")
print(x_tochn)