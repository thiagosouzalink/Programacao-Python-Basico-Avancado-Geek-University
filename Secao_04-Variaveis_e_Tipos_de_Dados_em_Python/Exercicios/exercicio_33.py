"""
33. Leia o tamanho do lado de um quadrado e imprima como resultado a
sua área.
"""

try:
    lado = float(input("Digite o valor do lado do quadrado: "))
except ValueError:
    print("O valor deve ser um número inteiro ou decimal.")
else:
    area = lado * lado
    print(f"Lado: {lado}")
    print(f"Área do quadrado: {area:.2f}")
