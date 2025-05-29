def obtener_minimo_palindromos(cadena):
    n =  len(cadena)
    OPT = [0] * (n+1)

    for i in range(1, n+1):
        minimo = float('inf')
        for j in range(0, i):
            if es_palindromo(cadena[j:i]):
                minimo = min(minimo, OPT[j] + 1)
        OPT[i] =  minimo
    return OPT[n]


def es_palindromo(s):
    return s == s[::-1]

