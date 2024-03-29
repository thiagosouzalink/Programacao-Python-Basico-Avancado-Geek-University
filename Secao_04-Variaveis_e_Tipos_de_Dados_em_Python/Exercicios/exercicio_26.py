"""
26. Leia um valor de área em metros quadrados m² e apresente-o 
convertido em hectares. A fórmula de conversão é: H = M * 0.0001, sendo
M a área em metros quadrados e H a área em hectares.
"""

try:
    m = float(input("Digite o valor da área em metro(s) quadrado(s): "))
except ValueError:
    print("O valor da área deve ser do tipo ponto flutuante.")
else:
    h = m * 0.0001
    print(f"Área em metros(s) quadrado(s): {m:.4f}")
    print(f"Área em hectares: {h:.4f}")
