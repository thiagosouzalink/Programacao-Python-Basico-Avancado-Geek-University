"""
24. Leia um valor de área em metros quadrados m² e apresente-o
convertido em acres. A fórmula da conversão é: A = M * 0.000247, sendo
M a área em metros quadrados e A a área em acres.
"""

try:
    m = float(input("Digite o valor da área em metros quadrados: "))
except ValueError:
    print("O valor da área deve ser do tipo ponto flutuante.")
else:
    a = m * 0.000247
    print(f"Área em metros(s) quadrado(s): {m:.4f}")
    print(f"Área em acres: {a:.4f}")
