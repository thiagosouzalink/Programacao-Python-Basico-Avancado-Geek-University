"""
3. Peça ao usuário para digitar três valores inteiros e imprima a
soma deles
"""

try:
    number1 = int(input("Digite o primeiro número inteiro: "))
    number2 = int(input("Digite o segundo número inteiro: "))
    number3 = int(input("Digite o terceiro número inteiro: "))
except ValueError:
    print("Apenas números inteiros são válidos.")
else:
    print(f"A soma entre números é: {number1 + number2 + number3}")
