import numpy as np

# Matrizes fornecidas
A = np.array([
    [1, 2, 3, 4, 5, 6, 7, 8],
    [2, 3, 4, 5, 6, 7, 8, 1],
    [3, 4, 5, 6, 7, 8, 1, 2],
    [4, 5, 6, 7, 8, 1, 2, 3],
    [5, 6, 7, 8, 1, 2, 3, 4],
    [6, 7, 8, 1, 2, 3, 4, 5],
    [7, 8, 1, 2, 3, 4, 5, 6],
    [8, 1, 2, 3, 4, 5, 6, 7]
])

B = np.array([
    [8, 7, 6, 5, 4, 3, 2, 1],
    [7, 6, 5, 4, 3, 2, 1, 8],
    [6, 5, 4, 3, 2, 1, 8, 7],
    [5, 4, 3, 2, 1, 8, 7, 6],
    [4, 3, 2, 1, 8, 7, 6, 5],
    [3, 2, 1, 8, 7, 6, 5, 4],
    [2, 1, 8, 7, 6, 5, 4, 3],
    [1, 8, 7, 6, 5, 4, 3, 2]
])

# Função para multiplicar duas matrizes
def matrix_multiplication(A, B):
    # Dimensões das matrizes
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])
    
    # Verificar se as matrizes podem ser multiplicadas
    if cols_A != rows_B:
        raise ValueError("Número de colunas de A deve ser igual ao número de linhas de B.")
    
    # Inicializar a matriz de resultado com zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    # Multiplicação de matrizes usando loops aninhados
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

# Multiplicar as matrizes A e B
result = matrix_multiplication(A, B)

# Exibir o resultado da multiplicação
for row in result:
    print(row)
