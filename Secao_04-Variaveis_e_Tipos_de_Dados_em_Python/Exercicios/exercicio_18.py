"""
18. Leia um valor de volume em metros cúbicos (m³) e apresente-o em
litros. A fórmula da conversão é L = 1000 * M, sendo L o volume em
litros e M o volume em metros cúbicos.
"""

try:
    m = float(input("Digite o volume em metros cúbicos: "))
except ValueError:
    print("O valor do volume deve ser do tipo ponto flutuante.")
else:
    l = 1000 * m
    print(f"Volume em metros cúbicos: {m:.4f}")
    print(f"Volume em litros: {l:.4f}")
