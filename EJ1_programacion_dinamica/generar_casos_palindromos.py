import string
import random
import os

CARPETA_CASOS = 'casos_palindromos'
SEMILLA = 42
random.seed(SEMILLA)  # Para reproducibilidad


# en este archivo se generan casos de prueba para el problema de conseguir la minima cantidad de palindromos de una cadena 


def generar_cadena_aleatoria(longitud):
    return ''.join(random.choices(string.ascii_lowercase, k=longitud))


def guardar_caso(nombre, q_values):
    path_general = os.path.join("EJ1_programacion_dinamica", CARPETA_CASOS)
    if not os.path.exists(path_general):
        os.makedirs(path_general)
    path = os.path.join("EJ1_programacion_dinamica", CARPETA_CASOS, f"{nombre}.txt")
    with open(path, 'w') as f:
        f.write(q_values)
    print(f"Caso guardado: {path}")


def generar_caso_para_tamano(n):
    casos = {
        f"{n}_aleatorio": lambda n=n: generar_cadena_aleatoria(n),

       
    }
    for nombre, generador in casos.items():
        guardar_caso(nombre, generador(n))

def generar_todos_los_casos():
    for n in range(50, 1050, 50):
        generar_caso_para_tamano(n)

if __name__ == "__main__":
    generar_todos_los_casos()