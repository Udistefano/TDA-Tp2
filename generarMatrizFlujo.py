import random

def generar_matriz_simetrica(n, min_val=1, max_val=20):
    matriz = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):
            val = random.randint(min_val, max_val)
            matriz[i][j] = val
            matriz[j][i] = val
    return matriz

def guardar_dataset(nombre_archivo, matriz, D, k, b):
    n = len(matriz)
    with open(nombre_archivo, 'w') as f:
        f.write(f"{n} {D} {k} {b}\n")
        for fila in matriz:
            f.write(' '.join(map(str, fila)) + '\n')

# Parámetros
n = 100
D = 80
k = 20
b = 30
random.seed(42)  # Fijamos semilla para reproducibilidad

matriz = generar_matriz_simetrica(n)
guardar_dataset("casos_red_de_flujo/matriz5.txt", matriz, D, k, b)
