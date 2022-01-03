"""
13. Leia uma distância em quilômetros e apresente-a convertida em
milhas.
A fórmula da conversão é M = K / 1,61, sendo K a distância em
quilômetros e M em milhas.
"""
try:
    k = float(input("Digite a distância em quilômetros: "))
except ValueError:
    print("A distância deve ser do tipo ponto flutuante.")
else:
    m = k / 1.61
    print(f"Distância em quilômetros: {k:.2f}")
    print(f"Distância em milhas: {m:.2f}")
