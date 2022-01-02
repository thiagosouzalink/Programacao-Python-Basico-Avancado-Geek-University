"""
10. Leia uma velocidade em Km/h (quilômetros por hora) e apresente-a
convertida em m/s (metros por segundo). A fórmula de conversão é:
M = K / 3.6, sendo K em Km/h e M em m/s.
"""

try:
    k = float(input("Digite a velocidade em Km/h: "))
except ValueError:
    print("A velocidade deve ser do tipo ponto flutuante.")
else:
    m = k / 3.6
    print(f"Valor em Km/h: {k:.2f}")
    print(f"Valor em m/s: {m:.2f}")
