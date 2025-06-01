import matplotlib.pyplot as plt
import csv
import os
from collections import defaultdict
import numpy as np

def graficar_ej1(path_csv):
    datos = defaultdict(list)

    with open(path_csv, 'r') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            caso = fila['Caso']
            tamanio = int(fila['Tamaño'])
            tiempo = float(fila['Tiempo'])

            tipo = caso.split('_')[-1]  # aleatorio, constantes, etc.
            datos[tipo].append((tamanio, tiempo))

    fig, ax = plt.subplots(figsize=(10, 5))
    for tipo, valores in datos.items():
        valores.sort()  # ordenar por tamaño
        tamanios = [v[0] for v in valores]
        tiempos = [v[1] for v in valores]
        ax.plot(tamanios, tiempos, marker='o', label=tipo.capitalize())

    ax.set_xlabel('Longitud de cadena')
    ax.set_ylabel('Tiempo (s)')
    ax.set_title('Obtener mínima cantidad de palíndromos - Tiempo de ejecución por longitud de cadena')
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.legend()
    plt.tight_layout()
    plt.show()


def graficar_ajuste_teorico_ej1(path_csv):
    tamanios = []
    tiempos = []

    with open(path_csv, 'r') as f:
        reader = csv.DictReader(f)
        for fila in reader:
            caso = fila['Caso']
            tipo = caso.split('_')[-1]
            if tipo == "aleatorio":  
                tamanios.append(int(fila['Tamaño']))
                tiempos.append(float(fila['Tiempo']))


    pares = sorted(zip(tamanios, tiempos))
    tamanios = np.array([x[0] for x in pares])
    tiempos = np.array([x[1] for x in pares])

    # Normalización para comparar contra n^3
    n3 = tamanios ** 3
    factor = tiempos[-1] / n3[-1]  # ajustar en el último punto para mejor visualización
    curva_teorica = factor * n3


    plt.figure(figsize=(8, 6))
    plt.plot(tamanios, tiempos, 'o-', label='Tiempos reales (aleatorio)', color='blue')
    plt.plot(tamanios, curva_teorica, '--', label='Curva teórica O(n³)', color='red')
    plt.xlabel("Tamaño de la cadena (n)")
    plt.ylabel("Tiempo de ejecución (s)")
    plt.title("Comparación entre tiempos reales y curva teórica O(n³)")
    plt.yscale('linear')
    plt.legend()
    plt.grid(True, which="both", linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()



if __name__ == "__main__":
    path_ej1 = os.path.join("EJ1_programacion_dinamica", "casos_palindromos", "tiempos_problema_1.csv")

    graficar_ej1(path_ej1)
    graficar_ajuste_teorico_ej1(path_ej1)
