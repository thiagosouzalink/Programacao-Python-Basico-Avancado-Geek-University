"""
35. Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida
pela equação: hipotenusa = sqrt(a² + b²). Faça um programa que receba os
valores de a e b e calcule o valor da hipotenusa através da equação.
Imprima o resultado dessa equação.
"""
import math

try:
    a = float(input("Digite o valor do primeiro cateto: "))
    b = float(input("Digite o valor do segundo cateto: "))
except ValueError:
    print("O valor deve ser um número inteiro ou decimal.")
else:
    hipotenusa = math.sqrt(a*a + b*b)
    print(f"Valores dos catetos: {a}, {b}")
    print(f"Valor da hipotenusa: {hipotenusa:.2f}")
