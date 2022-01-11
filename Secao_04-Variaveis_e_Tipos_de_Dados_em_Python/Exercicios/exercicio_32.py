"""
32. Leia um número inteiro e imprima a soma do sucessor de seu triplo
com o antecessor de seu dobro.
"""

try:
    numero = int(input("Digite o valor de um número inteiro: "))
except ValueError:
    print("O valor deve ser um número inteiro.")
else:
    sucessor_triplo = 3 * numero + 1
    antecessor_dobro = 2 * numero - 1
    soma = sucessor_triplo + antecessor_dobro
    print(f"Número: {numero}")
    print(f"Sucessor do seu triplo: {sucessor_triplo}")
    print(f"Antecessor do seu dobro: {antecessor_dobro}")
    print(f"Soma: {soma}")
