"""
29. Leia quatro notas, calcule a média aritmética e imprima o resultado
"""

try:
    num1 = float(input("Digite o valor do primeiro número: "))
    num2 = float(input("Digite o valor do segundo número: "))
    num3 = float(input("Digite o valor do terceiro número: "))
    num4 = float(input("Digite o valor do quarto número: "))
except ValueError:
    print("O valor deve ser um número inteiro ou fracional.")
else:
    media = (num1 + num2 + num3 + num4) / 4
    print(f"A média aritmética é: {media:.2f}")
