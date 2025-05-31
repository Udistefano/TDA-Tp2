import ejRedFlujo

def leerDatasetDesdeArchivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        
        # Primera línea: n D k b
        n, D, k, b = map(int, lineas[0].strip().split())

        # Siguientes n líneas: matriz de distancias
        distancias = []
        for i in range(1, n+1):
            fila = list(map(int, lineas[i].strip().split()))
            distancias.append(fila)

    return distancias, D, k, b, n

nombre_archivo = "casos_red_de_Flujo/matriz6.txt"
distancias, D, k, b, n = leerDatasetDesdeArchivo(nombre_archivo)

resultado = ejRedFlujo.asignarBackupsAntenas(distancias, D, k, b, n)
print("Conjuntos de backups por antena:")
if isinstance(resultado, str):
    print(resultado)
else:
    for i in range(len(resultado)):
        backup = resultado[i]
        print("Antena " + str(i+1) + ": " + "tiene como backup la antena " + str(backup))