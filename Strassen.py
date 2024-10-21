import numpy as np

def strassen(A, B): #função recursiva para multiplicar duas matrizes utilizando o algoritmo de Strassen.

    n = len(A)
    
    # caso base: quando a matriz é 1x1
    if n == 1: 
        return A * B
    
    else:
        # divisão das matrizes em submatrizes
        mid = n // 2
        
        A11 = A[:mid, :mid]
        A12 = A[:mid, mid:]
        A21 = A[mid:, :mid]
        A22 = A[mid:, mid:]
        B11 = B[:mid, :mid]
        B12 = B[:mid, mid:]
        B21 = B[mid:, :mid]
        B22 = B[mid:, mid:]

        #cálculo das sete matrizes M1 a M7
        M1 = strassen(A11 + A22, B11 + B22)
        M2 = strassen(A21 + A22, B11)
        M3 = strassen(A11, B12 - B22)
        M4 = strassen(A22, B21 - B11)
        M5 = strassen(A11 + A12, B22)
        M6 = strassen(A21 - A11, B11 + B12)
        M7 = strassen(A12 - A22, B21 + B22)
        
        # cálculo das submatrizes do resultado C
        
        C11 = M1 + M4 - M5 + M7
        C12 = M3 + M5
        C21 = M2 + M4
        C22 = M1 - M2 + M3 + M6
        
        # combinação das submatrizes para formar a matriz resultante C
        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
        
        return C

# exemplo de uso
if __name__ == "__main__":
    # definição das matrizes A e B de 8x8
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

    # multiplicação das matrizes usando o algoritmo de Strassen
    C = strassen(A, B)

    # exibição do resultado
    print("Matriz Resultante C:")
    print(C)
