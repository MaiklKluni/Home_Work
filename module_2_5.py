import random

def get_matrix(n,m,value):
    matrix = []
    for stroka in range(n):
        matrix.append([])
        for stolbec in range(m):
            matrix[stroka].append(value)
    return matrix

print(get_matrix(2,2,10))
print(get_matrix(3,5,42))
print(get_matrix(4,2,13))