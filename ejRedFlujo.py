# Hecho por chat gpt basado en el pseudocodigo, no se si es necesario implementarlo

def existe_camino_residual(grafo, flujo, origen, destino, padres):
    """Busca un camino aumentante en el grafo residual usando búsqueda por lista (sin deque)."""
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

def flujo_maximo_ford_fulkerson(grafo, origen, destino):
    """Implementación Ford-Fulkerson clásica con lista para BFS."""
    n = len(grafo)
    flujo = [[0]*n for _ in range(n)]
    padres = [-1]*n
    flujo_total = 0

    while existe_camino_residual(grafo, flujo, origen, destino, padres):
        # Encontrar capacidad mínima residual en el camino encontrado
        minimo_residual = float('inf')
        nodo = destino
        while nodo != origen:
            anterior = padres[nodo]
            residual = grafo[anterior][nodo] - flujo[anterior][nodo]
            if residual < minimo_residual:
                minimo_residual = residual
            nodo = anterior

        # Aumentar el flujo a lo largo del camino
        nodo = destino
        while nodo != origen:
            anterior = padres[nodo]
            flujo[anterior][nodo] += minimo_residual
            flujo[nodo][anterior] -= minimo_residual
            nodo = anterior

        flujo_total += minimo_residual

    return flujo_total, flujo

def asignar_backups_antenas(distancias, D, k, b, n):
    """
    Construye el grafo según el pseudocódigo y usa Ford-Fulkerson para asignar backups.
    distancias: matriz n x n con distancias entre antenas
    D, k, b, n: parámetros del problema
    """
    nodo_fuente = 0
    nodo_sumidero = 2*n + 1
    total_nodos = 2*n + 2

    # Crear grafo con capacidades inicializadas en 0
    grafo = [[0]*total_nodos for _ in range(total_nodos)]

    # Agregar aristas fuente -> Ai con capacidad k
    for i in range(1, n+1):
        grafo[nodo_fuente][i] = k

    # Agregar aristas Bi -> sumidero con capacidad b
    for i in range(n+1, 2*n+1):
        grafo[i][nodo_sumidero] = b

    # Agregar aristas Ai -> Bj si distancia < D y i != j con capacidad 1
    for i in range(n):
        for j in range(n):
            if i != j and distancias[i][j] < D:
                nodo_requisitor = i + 1
                nodo_servidor = j + n + 1
                grafo[nodo_requisitor][nodo_servidor] = 1

    # Ejecutar Ford-Fulkerson para flujo máximo
    flujo_total, flujo = flujo_maximo_ford_fulkerson(grafo, nodo_fuente, nodo_sumidero)

    # Verificar si se logró el flujo total esperado
    if flujo_total < n * k:
        return "No existe solución posible"

    # Construir conjunto backup para cada antena
    backups = [[] for _ in range(n)]
    for i in range(n):
        nodo_requisitor = i + 1
        for j in range(n):
            nodo_servidor = j + n + 1
            if flujo[nodo_requisitor][nodo_servidor] > 0:
                backups[i].append(j+1)  # antenas numeradas desde 1

    return backups

# Ejemplo de prueba
distancias = [
    [0, 2, 3, 4],
    [2, 0, 1, 5],
    [3, 1, 0, 2],
    [4, 5, 2, 0]
]

D = 3
k = 1
b = 2
n = 4

resultado = asignar_backups_antenas(distancias, D, k, b, n)
print("Conjuntos backup por antena:")
if isinstance(resultado, str):
    print(resultado)
else:
    for i, backup in enumerate(resultado, 1):
        print(f"Antena {i}: {backup}")
