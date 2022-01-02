"""
2. Faça um programa que leia um número real e o imprima.
"""

try:
    number = float(input("Digite um número em ponto flutuante: "))
except ValueError:
    print("O valor digitado deve ser um número em ponto flutuante.")
else:
    print(number)
