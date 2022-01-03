"""
19. Leia um valor de volume em litros e apresente-o em metros cúbicos.
A fórmula da conversão é M = L / 1000, sendo L o volume em litros e M o
volume em metros cúbicos.
"""

try:
    l = float(input("Digite o volume em litros: "))
except ValueError:
    print("O valor do volume deve ser do tipo ponto flutuante.")
else:
    m = l / 1000
    print(f"Volume em litros: {l:.4f}")
    print(f"Volume em metros cúbicos: {m:.4f}")
