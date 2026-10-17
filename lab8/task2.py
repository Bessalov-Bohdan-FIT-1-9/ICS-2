import numpy as np

n = int(input("Введіть число N: "))

matrix = np.zeros((n, n), dtype=int)
value = n * n
for i in range(n):
    for j in range(n):
        matrix[i][j] = value
        value = value - 1

print(matrix)