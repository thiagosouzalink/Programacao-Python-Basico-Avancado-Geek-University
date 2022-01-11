"""
31. Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
"""

try:
    numero = int(input("Digite o valor de um número inteiro: "))
except ValueError:
    print("O valor deve ser um número inteiro.")
else:
    antecessor = numero - 1
    sucessor = numero + 1
    print(f"Número: {numero}")
    print(f"Antecessor: {antecessor}")
    print(f"Sucessor: {sucessor}")
