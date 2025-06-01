import pulp

prob = pulp.LpProblem("Publicidad_Paradas", pulp.LpMaximize)

# Variables binarias
A = pulp.LpVariable("A", cat='Binary')
B1 = pulp.LpVariable("B1", cat='Binary') 
B2 = pulp.LpVariable("B2", cat='Binary')
C = pulp.LpVariable("C", cat='Binary')
D = pulp.LpVariable("D", cat='Binary')
E = pulp.LpVariable("E", cat='Binary')
F = pulp.LpVariable("F", cat='Binary')
G = pulp.LpVariable("G", cat='Binary')

prob += 50000*A + 100000*B1 + 120000*B2 + 100000*C + 80000*D + 5000*E + 40000*F + 90000*G

prob += 30*A + 80*B1 + 120*B2 + 75*C + 50*D + 2*E + 20*F + 100*G <= 200  
prob += B1 + B2 <= 1 
prob += A + D <= 1  

prob.solve()

resultado = f"Beneficio máximo: ${pulp.value(prob.objective):,.0f}\n"
resultado += f"A: {pulp.value(A)}, B1: {pulp.value(B1)}, B2: {pulp.value(B2)}, C: {pulp.value(C)}\n"
resultado += f"D: {pulp.value(D)}, E: {pulp.value(E)}, F: {pulp.value(F)}, G: {pulp.value(G)}"

with open("resultado_paradas.txt", "w") as archivo:
    archivo.write(resultado)

print(resultado)
print("\nResultado guardado en: resultado_paradas.txt")