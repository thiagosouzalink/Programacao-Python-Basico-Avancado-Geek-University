"""
37. Faça um programa que leia o valor de um produto e imprima o valor
com desconto, tendo em vista que o desconto foi de 12%
"""

try:
    produto = float(input("Digite o valor do produto: "))
except ValueError:
    print("O valor deve ser um número inteiro ou decimal.")
else:
    DESCONTO = 0.12
    valor_final = produto - produto*DESCONTO
    print(f"Valor incial do produto: R$ {produto:.2f}")
    print(f"desconto: {int(DESCONTO*100)}%")
    print(f"Valor final com desconto: R$ {valor_final:.2f}")
