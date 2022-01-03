"""
16. Leia um valor de comprimento em polegadas e apresente-o convertido
em centímetros. A fórmula de conversão é C = P * 2.54, sendo C o
comprimento em centímetros e P o comprimento em polegadas.
"""

try:
    p = float(input("Digite o comprimento em polegadas: "))
except ValueError:
    print("O valor do comprimento deve ser do tipo ponto flutuante.")
else:
    c = p * 2.54
    print(f"Comprimento em polegadas: {p:.2f}")
    print(f"Comprimento em centímetros: {c:.2f}")
