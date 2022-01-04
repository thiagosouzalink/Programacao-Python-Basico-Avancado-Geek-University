"""
22. Leia um valor de comprimento em metros e apresente-o convertido em
jardas. A fórmula de conversão é: J = M / 0.91, sendo J o comprimento em
jardas e M o comprimento em metros.
"""

try:
    m = float(input("Digite o valor do comprimento em metro(s): "))
except ValueError:
    print("O valor do comprimento deve ser do tipo ponto flutuante.")
else:
    j = m / 0.91
    print(f"Comprimento em metro(s): {m:.2f}")
    print(f"Comprimento em jarda(s): {j:.2f}")
