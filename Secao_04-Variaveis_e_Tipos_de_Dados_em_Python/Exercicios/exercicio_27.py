"""
27. Leia um valor de área em hectares e apresente-o convertido em metros
quadrados m². A fórmula de conversão é: M = H * 10000, sendo M a área em
metros quadrados e H a área em hectares.
"""

try:
    h = float(input("Digite o valor da área em hectares: "))
except ValueError:
    print("O valor da área deve ser do tipo ponto flutuante.")
else:
    m = h * 10000
    print(f"Área em hectares: {h:.4f}")
    print(f"Área em metros(s) quadrado(s): {m:.4f}")
