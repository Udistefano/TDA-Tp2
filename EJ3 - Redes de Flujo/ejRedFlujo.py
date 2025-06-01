# Implementación del algoritmo Ford-Fulkerson para el problema de asignación de backups a antenas
def existeCaminoResidual(grafo, flujo, origen, destino, padres):
    visitados = [False] * len(grafo)
    cola = [origen]
    visitados[origen] = True
    while cola:
        actual = cola.pop(0)
        for vecino in range(len(grafo)):
            capacidad_residual = grafo[actual][vecino] - flujo[actual][vecino]
            if capacidad_residual > 0 and not visitados[vecino]:
                cola.append(vecino)
                visitados[vecino] = True
                padres[vecino] = actual
                if vecino == destino:
                    return True
    return False

# Implementación Ford-Fulkerson clásica para BFS.
def flujoMaxFordFulkerson(grafo, origen, destino):
    n = len(grafo)
    flujo = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(0)
        flujo.append(fila)
    padres = [-1]*n
    flujoTotal = 0

    while existeCaminoResidual(grafo, flujo, origen, destino, padres):
        # Encontrar capacidad mínima residual 
        minimoResidual = float('inf')
        nodo = destino
        while nodo != origen:
            anterior = padres[nodo]
            residual = grafo[anterior][nodo] - flujo[anterior][nodo]
            if residual < minimoResidual:
                minimoResidual = residual
            nodo = anterior

        # Aumentar el flujo a lo largo del camino
        nodo = destino
        while nodo != origen:
            anterior = padres[nodo]
            flujo[anterior][nodo] += minimoResidual
            flujo[nodo][anterior] -= minimoResidual
            nodo = anterior

        flujoTotal += minimoResidual

    return flujoTotal, flujo

 # Construye el grafo y usa Ford-Fulkerson para asignar backups.
def asignarBackupsAntenas(distancias, D, k, b, n):
    nodoFuente = 0
    nodoSumidero = 2*n + 1
    totalNodos = 2*n + 2
    grafo = []
    for i in range(totalNodos):  # Crear grafo 
        fila = []
        for j in range(totalNodos):
            fila.append(0)
        grafo.append(fila)

    # Agrega aristas fuente -> Ai con capacidad k
    for i in range(1, n+1):
        grafo[nodoFuente][i] = k

    # Agrega aristas Bi al sumidero con capacidad b
    for i in range(n+1, 2*n+1):
        grafo[i][nodoSumidero] = b

    # Agrega aristas Ai a Bj si distancia < D y ademas i != j con capacidad 1
    for i in range(n):
        for j in range(n):
            if i != j and distancias[i][j] < D:
                nodoEntrada = i + 1
                nodoSalida = j + n + 1
                grafo[nodoEntrada][nodoSalida] = 1

    # Ejecuta Ford-Fulkerson para flujo max 
    flujoTotal, flujo = flujoMaxFordFulkerson(grafo, nodoFuente, nodoSumidero)

    # Verifica si se logró el flujo total esperado
    if flujoTotal < n * k:
        return "No existe solución posible"

    backups = []
    for i in range(n):    # backup para cada antena
        backups.append([])
        
    for i in range(n):
        nodoEntrada = i + 1
        for j in range(n):
            nodoSalida = j + n + 1
            if flujo[nodoEntrada][nodoSalida] > 0:
                backups[i].append(j+1)  # antenas numeradas desde la 1era

    return backups
