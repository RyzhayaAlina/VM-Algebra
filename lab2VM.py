import numpy as np
# вариант 13 (т.е. 3)

n=3
# тест номер 3
# A=np.array([[5, 2, 3],
#             [1, 6, 1],
#             [3, -4, -2]])
# b=np.array([[3], [5], [8]])
# x_tochn=np.array([[2], [1], [-3]])

# СЛАУ 1
# A=np.array([[13.14, -2.12, 1.17],
#             [-2.12, 6.3, -2.45],
#             [1.17, -2.45, 4.6]])
# b=np.array([[1.27], [2.13], [3.14]])
# x_tochn=np.linalg.solve(A, b)

# СЛАУ 2
A=np.array([[4.31, 0.26, 0.61, 0.27],
            [0.26, 2.32, 0.18, 0.34],
            [0.61, 0.18, 3.20, 0.31],
            [0.27, 0.34, 0.31, 5.17]])
b=np.array([[1.02], [1.00], [1.34], [1.27]])
x_tochn=np.linalg.solve(A, b)
n+=1

L=np.zeros((n,n))
U=np.zeros((n,n))

# заполнение матриц
for j in range(n):
    U[0, j]=A[0, j]
for i in range(n):
    L[i, 0]=A[i, 0]/U[0, 0]

for i in range(1, n):
    for j in range(1, n):
        if i<=j:
            U[i, j]=A[i, j]-sum([L[i, k]* U[k, j] for k in range(i)])
            if i==j:
                L[i, j]=1
        if i>j:
            L[i, j]=(A[i, j]-sum([L[i, k]* U[k, j] for k in range(j)]))/U[j, j]

print("Матрица U: ")
print(U)
print("Матрица L: ")
print(L)

# Проверка
print("Произведение: ")
print(L @ U )
print("Ориганальная А: ")
print(A)

# получение решения
y = np.linalg.solve(L, b)
x_solve = np.linalg.solve(U, y)
print("Приблеженное решение: ")
print(x_solve)
print("Точное решение: ")
print(x_tochn)