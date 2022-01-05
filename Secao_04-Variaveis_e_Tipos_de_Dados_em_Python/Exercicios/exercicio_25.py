"""
25. Leia um valor de área em acres e apresente-o convertido em metros
quadrados m². A fórmula da conversão é: M = A * 4048.58, sendo
M a área em metros quadrados e A a área em acres.
"""

try:
    a = float(input("Digite o valor da área em acre(s): "))
except ValueError:
    print("O valor da área deve ser do tipo ponto flutuante.")
else:
    m = a * 4048.58
    print(f"Área em acre(s): {a:.4f}")
    print(f"Área em metros(s) quadrado(s): {m:.4f}")
