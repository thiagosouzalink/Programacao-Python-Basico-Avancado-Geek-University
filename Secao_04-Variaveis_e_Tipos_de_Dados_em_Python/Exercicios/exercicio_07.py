"""
7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em
graus Celsius.
A Fórmula da conversão é: C = 5.0 * (F-32.0) / 9.0, sendo C a
temperatura em Celsius e F a temperatura em Fahrenheit.
"""

try:
    f = float(input("Digite a temperatura em grau(s) Fahrenheit: "))
except ValueError:
    print("A temperatura deve ser do tipo ponto flutuante.")
else:
    c = 5.0 * (f - 32) / 9.0
    print(f"Valor em grau(s) Fahrenheit: {f:.2f}")
    print(f"Valor em grau(s) Celsius: {c:.2f}")
