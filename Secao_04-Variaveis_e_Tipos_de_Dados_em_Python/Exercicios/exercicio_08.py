"""
8. Leia uma temperatura em graus Kelvin e apresente-a convertida em
graus Celsius.
A Fórmula da conversão é: C = K - 273.15, sendo C a temperatura em
Celsius e K a temperatura em Kelvin.
"""

try:
    k = float(input("Digite a temperatura em grau(s) Kelvin: "))
except ValueError:
    print("A temperatura deve ser do tipo ponto flutuante.")
else:
    c = k - 273.15
    print(f"Valor em grau(s) Kelvin: {k:.2f}")
    print(f"Valor em grau(s) Celsius: {c:.2f}")
