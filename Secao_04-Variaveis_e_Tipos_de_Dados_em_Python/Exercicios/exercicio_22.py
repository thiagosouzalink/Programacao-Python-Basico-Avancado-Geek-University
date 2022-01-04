"""
22. Leia um valor de comprimento em jardas e apresente-o convertido em
metros. A fórmula de conversão é: M = 0,91 * J, sendo J o comprimento em
jardas e M o comprimento em metros.
"""

try:
    j = float(input("Digite o valor do comprimento em jarda(s): "))
except ValueError:
    print("O valor do comprimento deve ser do tipo ponto flutuante.")
else:
    m = 0.91 * j
    print(f"Comprimento em jarda(s): {j:.2f}")
    print(f"Comprimento em metro(s): {m:.2f}")
