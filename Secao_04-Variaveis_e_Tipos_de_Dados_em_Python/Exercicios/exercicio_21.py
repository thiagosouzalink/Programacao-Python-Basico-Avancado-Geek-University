"""
21. Leia um valor de massa em libras e apresente-o convertido em
quilogramas. A fórmula de conversão é K = L * 0.45, sendo K a massa em
quilogramas e L a massa em libras.
"""

try:
    l = float(input("Digite o valor da massa em libra(s): "))
except ValueError:
    print("O valor da massa deve ser do tipo ponto flutuante.")
else:
    k = l * 0.45
    print(f"Massa em libras: {l:.2f}")
    print(f"Massa em quilogramas: {k:.2f}")
