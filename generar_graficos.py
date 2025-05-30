import matplotlib.pyplot as plt
import csv
import os
from collections import defaultdict


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

    ax.set_xlabel('Tamaño')
    ax.set_ylabel('Tiempo (s)')
    ax.set_title('Ejercicio 1 - Tiempo de ejecución por tipo de entrada')
    ax.grid(True, linestyle='--', linewidth=0.5)
    ax.legend()
    plt.tight_layout()
    plt.show()




if __name__ == "__main__":
    path_ej1 = os.path.join("casos_palindromos", "tiempos_problema_1.csv")

    graficar_ej1(path_ej1)
