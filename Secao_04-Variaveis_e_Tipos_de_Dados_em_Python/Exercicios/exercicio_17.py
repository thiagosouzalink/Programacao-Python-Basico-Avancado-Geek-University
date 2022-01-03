"""
17. Leia um valor de comprimento em centímetros e apresente-o convertido
em polegadas. A fórmula de conversão é P = C / 2.54, sendo C o
comprimento em centímetros e P o comprimento em polegadas.
"""

try:
    c = float(input("Digite o comprimento em centímetros: "))
except ValueError:
    print("O valor do comprimento deve ser do tipo ponto flutuante.")
else:
    p = c / 2.54
    print(f"Comprimento em centímetros: {c:.2f}")
    print(f"Comprimento em polegadas: {p:.2f}")
