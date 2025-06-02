# TDA-Tp2
TP2 -Teoria de algoritmos - Echeverría

Link del informe: https://docs.google.com/document/d/1-sp4cZSwZibb0N5aIRMJu3j4yQnjoygoP9CNl8guUPU/edit?usp=sharing

Integrantes: 
Dávila, Rebeca Analía | Padrón: 108672
Camilo Sassone Irrazabal | Padrón: 111135
Gabriela Yanes | Padrón: 108325
Ulises Distéfano | Padrón: 111883


## Información relevante:

- Lenguaje utilizado: Python
- Versión mínima utilizada: 3.8.10
- Bibliotecas utilizadas:
    - csv
    - os
    - collections
    - numpy
    - string
    - random
    - time 
    - matplotlib (pyplot)
    - pulp



## Instrucciones para ejecutar:

### ejercicio 1: programacion dinamica

* Generar casos de prueba:

Parado sobre la carpeta principal TDA-Tp2

- Para generar los casos de prueba aleatorios:
    - ´python3 EJ1_programacion_dinamica/generar_casos_palindromos.py´
    
    Se guardan dentro de la carpeta principal del ejercicio "EJ1_programacion_dinamica" en una carpeta llamada "casos_palindromos"

- Para ejecutar los casos de prueba y tomar el tiempo de cada uno:
    - ´python3 EJ1_programacion_dinamica/ejecutar_casos_palindromos.py´

    Se guardan en una carpeta llamada resultados dentro de casos_palindromos, dentro de EJ1_programacion_dinamica. Y tambien se agrega una archivo csv con cada caso y su tiempo.
- Para generar los graficos utilizando estos resultados:
    - ´python3 EJ1_programacion_dinamica/generar_graficos.py´

    Esto muestra los gráficos directamente pero se guardaron unos fijos en una carpteta llamada "graficos_tiempos"

### ejercicio 3: Redes de flujo

* Generar casos de prueba:

Parado sobre la carpeta principal TDA-Tp2

- Para generar los casos de prueba aleatorios:
    - ´python3 EJ3 - Redes de Flujo/generarMatrizFlujo.py´
    En ese archivo vamos a poder definir los parametros y construir matrices a partir de ellos.
    Se guardan dentro de la carpeta principal del ejercicio "EJ3 - Redes de Flujo" en una carpeta llamada "casos_red_de_flujo"

- Para ejecutar los casos de prueba y tomar el tiempo de cada uno:
    - ´python3 EJ3 - Redes de Flujo/ejecutarRedFlujo.py´
    Dentro de este codigo tenemos la variable "nombreArchivo" en la cual debemos poner la matriz que queremos ejecutar. Una vez corriendo este codigo, nos dará el resultado de cada antena con su backup
