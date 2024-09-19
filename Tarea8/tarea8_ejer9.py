def multiplicar_matrices(A, B):
    filas_A = len(A)
    columnas_A = len(A[0])
    filas_B = len(B)
    columnas_B = len(B[0])

    if columnas_A != filas_B:
        raise ValueError("El número de columnas de A debe ser igual al número de filas de B")

    resultado = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

    for i in range(filas_A):
        for j in range(columnas_B):
            for k in range(columnas_A):
                resultado[i][j] += A[i][k] * B[k][j]
            print(f"Resultado[{i}][{j}] = {resultado[i][j]}")  

    return resultado

A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

resultado = multiplicar_matrices(A, B)
print("Matriz resultado:")
for fila in resultado:
    print(fila)
