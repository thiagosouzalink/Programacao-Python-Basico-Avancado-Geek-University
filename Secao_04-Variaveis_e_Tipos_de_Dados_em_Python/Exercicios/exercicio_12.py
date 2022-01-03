"""
12. Leia uma distância em milhas e apresente-a convertida em
quilômetros.
A fórmula da conversão é K = 1,61 * M, sendo K a distância em
quilômetros e M em milhas.
"""
try:
    m = float(input("Digite a distância em milhas: "))
except ValueError:
    print("A distância deve ser do tipo ponto flutuante.")
else:
    k = 1.61 * m
    print(f"Distância em milhas: {m:.2f}")
    print(f"Distância em quilômetros: {k:.2f}")
