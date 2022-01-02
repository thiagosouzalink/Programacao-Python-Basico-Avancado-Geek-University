"""
1. Faça um programa que leia um número inteiro e o imprima.
"""

try:
    number = int(input("Digite um número inteiro: "))
except ValueError:
    print("O valor digitado deve ser um número inteiro.")
else:
    print(number)
