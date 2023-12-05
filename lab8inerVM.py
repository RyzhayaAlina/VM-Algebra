import numpy as np

# Метод нахождения наименьшего сз и его св

# A = np.array([[3, 5, 1],
#             [1, 10, 2],
#             [1, 1, 10]])

# A = np.array([[10, 2, 5, 3],
#               [2, 11, 8, 6],
#               [5, 8, 6, 9],
#               [3, 6, 9, 12]])

A = np.array([[6.22, 1.42, -1.72, 1.91],
            [1.42, 5.33, 1.11, -1.82],
            [-1.72, 1.11, 5.24, 1.42],
            [1.91, -1.82, 1.42, 6.55]])

n = (np.shape(A))[0]
I = np.eye(n)
e = 10**(-3)
flag = False
b = np.ones((n, 1))   # примерный св
alfa = 1   # примерное сз
k = 0
while not flag:
    b_new = np.copy(b)
    M = A - alfa * I
    b_new = (np.linalg.inv(M) @ b)/np.linalg.norm(M @ b)
    flag = np.linalg.norm(b_new-b) < e
    b = b_new
    k+=1

alfa_real = np.transpose(b) @ A @ b / (np.transpose(b) @ b)
print("Примерное наименьшее по модулю СЗ: ")
print(alfa_real)
print("Количество шагов для подсчета: ", k+1)
print("Наибольшее СЗ с помощью встроенной функции: ")
print(min(abs(np.linalg.eigvals(A))))
