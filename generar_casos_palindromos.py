import string
import random
import os

CARPETA_CASOS = 'casos_palindromos'
SEMILLA = 42
random.seed(SEMILLA)  # Para reproducibilidad


# en este archivo se generan casos de prueba para el problema de conseguir la minima cantidad de palindromos de una cadena 
# se generaran estos casos:
# 1. cadenas con caracteres aleatorios
# 2. cadenas con caracteres repetidos
# 3. cadenas que pueden ser palindromos

def generar_cadena_aleatoria(longitud):
    return ''.join(random.choices(string.ascii_lowercase, k=longitud))


def guardar_caso(nombre, q_values):
    if not os.path.exists(CARPETA_CASOS):
        os.makedirs(CARPETA_CASOS)
    path = os.path.join(CARPETA_CASOS, f"{nombre}.txt")
    with open(path, 'w') as f:
        f.write(q_values)
    print(f"Caso guardado: {path}")


def generar_casos_para_tamano(n):
    casos = {
        f"{n}_aleatorio": lambda n=n: generar_cadena_aleatoria(n),

       
    }
    for nombre, generador in casos.items():
        guardar_caso(nombre, generador(n))

def generar_todos_los_casos():
    for n in [5, 10, 15, 20, 25, 30]:
        generar_casos_para_tamano(n)

if __name__ == "__main__":
    generar_todos_los_casos()