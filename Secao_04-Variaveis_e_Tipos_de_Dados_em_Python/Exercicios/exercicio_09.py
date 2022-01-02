"""
9. Leia uma temperatura em graus Celsius e apresente-a convertida em
graus Kelvin.
A Fórmula da conversão é: K = c + 273.15, sendo C a temperatura em
Celsius e K a temperatura em Kelvin.
"""

try:
    c = float(input("Digite a temperatura em grau(s) Celsius: "))
except ValueError:
    print("A temperatura deve ser do tipo ponto flutuante.")
else:
    k = c - 273.15
    print(f"Valor em grau(s) Celsius: {c:.2f}")
    print(f"Valor em grau(s) Kelvin: {k:.2f}")
