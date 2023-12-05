import numpy as np

# Метод вращений для поиска СЗ

def func_max_element(A, n):
    max = -1
    ki = 0
    kj = 0
    for i in range(n):
        for j in range(n):
            if i!=j:
                if abs(A[i, j])>max:
                    max = A[i, j]
                    ki = i
                    kj = j
    return(abs(max), ki, kj)

def func_rot(A, n, i, j):
    if A[i, i]!=A[j, j]:
        fi = 0.5 * np.arctan(2*A[i, j]/(A[i, i]-A[j, j]))
    else: fi = np.pi/4
    R = np.eye(n)
    R[i, i] = np.cos(fi)
    R[i, j] = -np.sin(fi)
    R[j, i] = np.sin(fi)
    R[j, j] = np.cos(fi)
    A_new = np.transpose(R) @ A @ R
    return(A_new)

n = 4
A = np.array([[10, 2, 5, 3],
              [2, 11, 8, 6],
              [5, 8, 6, 9],
              [3, 6, 9, 12]])

# n = 5
# A = np. array([[2, 1, 4, 3, 5],
#                [1, 6, 2, 1, -1,],
#                [4, 2, 9, 6, 3],
#                [3, 1, 6, 8, 2],
#                [5, -1, 3, 2, 10]])
e = 10**(-5)
conf = False
k =0
while not conf:
    F = func_max_element(A, n)
    A_new = func_rot(A, n, F[1], F[2])
    conf = F[0] < e
    A = A_new
    k+=1
print("Собсвенные значения матрицы: ")
[print(A[t, t]) for t in range(n)]
print("Собственные значения матрицы с помощью встроенной функции: ")
print(np.linalg.eigvals(A))
print(k)
