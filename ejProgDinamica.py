def obtener_minimo_palindromos(cadena):
    n =  len(cadena)
    OPT = [0] * (n+1)
    OPT[0] = 0
    OPT[1] = 1

    for i in range(2, n+1):
        minimo = float('inf')
        for j in range(0, i+1):
            if es_palindromo(cadena[j:i]):
                minimo = min(minimo, OPT[j] + 1)
        OPT[i] =  minimo
    return OPT[n]


def es_palindromo(s):
    return s == s[::-1]

