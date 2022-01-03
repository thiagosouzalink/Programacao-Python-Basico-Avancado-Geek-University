"""
14. Leia um ângulo em graus e apresente-o convertido em radianos. A
fórmula de conversão é: R = G * PI/180, sendo G o ângulo em graus e R em
radianos e PI = 3.14
"""
import math


try:
    g = float(input("Digite o ângulo em graus: "))
except ValueError:
    print("O valor do ângulo deve ser do tipo ponto flutuante.")
else:
    r = g * math.pi / 180
    print(f"Ângulo em graus: {g:.2f}")
    print(f"Ângulo em radianos: {r:.2f}")
