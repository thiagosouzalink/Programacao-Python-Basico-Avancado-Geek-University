"""
11. Leia uma velocidade em m/s (metros por segundo) e apresente-a
convertida em Km/h (quilômetros por hora). A fórmula de conversão é:
K = M * 3.6, sendo K em Km/h e M em m/s.
"""

try:
    m = float(input("Digite a velocidade em m/s: "))
except ValueError:
    print("A velocidade deve ser do tipo ponto flutuante.")
else:
    k = m * 3.6
    print(f"Valor em m/s: {m:.2f}")
    print(f"Valor em Km/h: {k:.2f}")
