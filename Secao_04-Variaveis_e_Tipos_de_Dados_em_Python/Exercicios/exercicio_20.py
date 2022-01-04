"""
20. Leia um valor de massa em quilogramas e apresente-o convertido em
libras. A fórmula de conversão é L = K / 0.45, sendo K a massa em
quilogramas e L a massa em libras.
"""

try:
    k = float(input("Digite o valor da massa em quilograma(s): "))
except ValueError:
    print("O valor da massa deve ser do tipo ponto flutuante.")
else:
    l = k / 0.45
    print(f"Massa em quilogramas: {k:.2f}")
    print(f"Massa em libras: {l:.2f}")
