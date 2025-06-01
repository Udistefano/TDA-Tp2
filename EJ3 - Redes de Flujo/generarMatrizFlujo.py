import random
#Codigo para generar matrices
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

# parametros 
n = 460
D = 198
k = 74
b = 90
random.seed(42)  # semilla 

matriz = generar_matriz_simetrica(n)
guardar_dataset("casos_red_de_flujo/matriz8.txt", matriz, D, k, b)
