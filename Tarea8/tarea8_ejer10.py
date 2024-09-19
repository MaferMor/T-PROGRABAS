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
    
    return resultado

def potencia_matriz(matriz, exponente):
    if exponente == 1:
        return matriz
    elif exponente % 2 == 0:
        mitad_potencia = potencia_matriz(matriz, exponente // 2)
        return multiplicar_matrices(mitad_potencia, mitad_potencia)
    else:
        return multiplicar_matrices(matriz, potencia_matriz(matriz, exponente - 1))

matriz = [
    [2, 0],
    [0, 2]
]

exponente = 3
resultado = potencia_matriz(matriz, exponente)

print(f"Matriz elevada a la potencia {exponente}:")
for fila in resultado:
    print(fila)
