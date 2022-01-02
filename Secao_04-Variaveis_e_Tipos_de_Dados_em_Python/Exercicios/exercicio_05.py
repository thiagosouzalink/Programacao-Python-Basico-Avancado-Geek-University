"""
5. Leia um número real e imprima a quinta parte deste número.
"""

try:
    number = float(input("Digite um número em ponto flutuante: "))
except ValueError:
    print("O valor digitado deve ser um número em ponto flutuante.")
else:
    print(f"O quinta parte do número {number:.2f} é: {number/5:.2f}")
