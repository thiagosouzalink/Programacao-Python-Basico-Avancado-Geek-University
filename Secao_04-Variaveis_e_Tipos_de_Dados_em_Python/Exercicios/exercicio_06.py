"""
6. Leia uma temperatura em graus Celsius e apresente-a convertida em
graus Fahrenheit.
A Fórmula da conversão é: F = C*(9.0/5.0) + 32.0, sendo F a temperatura
em Fahrenheit e C a temperatura em Celsius.
"""

try:
    c = float(input("Digite a temperatura em grau(s) Celsius: "))
except ValueError:
    print("A temperatura deve ser do tipo ponto flutuante.")
else:
    f = c * (9.0/5.0) + 32
    print(f"Valor em grau(s) Celsius: {c:.2f}")
    print(f"Valor em grau(s) Fahrenheit: {f:.2f}")
