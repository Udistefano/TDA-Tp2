import os
import time
import csv
# se calculan los resultados y tiempos para el problema 1 (pd-palindromos).

from ejProgDinamica import obtener_minimo_palindromos

CARPETA_CASOS = "casos_palindromos"
CARPETA_RESULTADOS = os.path.join("EJ1_programacion_dinamica", CARPETA_CASOS, "resultados")
ARCHIVO_TIEMPOS = os.path.join("EJ1_programacion_dinamica", CARPETA_CASOS, "tiempos_problema_1.csv")



if not os.path.exists(CARPETA_RESULTADOS):
    os.makedirs(CARPETA_RESULTADOS)

def leer_caso(path):
    with open(path, 'r') as f:
        linea = f.readline()
        return linea.strip()

def guardar_resultado(nombre, cantidad_minima):
    path = os.path.join(CARPETA_RESULTADOS, f"{nombre}.txt")
    with open(path, 'w') as f:
        f.write(str(cantidad_minima))

def main():
    tiempos = []
    path_general = os.path.join("EJ1_programacion_dinamica", CARPETA_CASOS)
    for archivo in sorted(os.listdir(path_general)):
        if not archivo.endswith(".txt"):
            continue
        nombre = archivo[:-4]
        path = os.path.join("EJ1_programacion_dinamica", CARPETA_CASOS, archivo)
        print(f"Procesando: {nombre}")

        q = leer_caso(path)
        inicio = time.time()
        cantidad_minima = obtener_minimo_palindromos(q)
        fin = time.time()

        duracion = fin - inicio
        tiempos.append((nombre, len(q), duracion))
        guardar_resultado(nombre, cantidad_minima)
        print(f"Tiempo: {duracion:.4f} segundos")

    # Guardar los tiempos
    with open(ARCHIVO_TIEMPOS, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Caso", "Tamaño", "Tiempo"])
        writer.writerows(tiempos)

if __name__ == "__main__":
    main()