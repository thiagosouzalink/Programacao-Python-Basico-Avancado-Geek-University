"""
15. Leia um ângulo em radianos e apresente-o convertido em graus. A
fórmula de conversão é: G = R * 180/PI, sendo G o ângulo em graus e R em
radianos e PI = 3.14
"""
import math


try:
    r = float(input("Digite o ângulo em radianos: "))
except ValueError:
    print("O valor do ângulo deve ser do tipo ponto flutuante.")
else:
    g = r * 180 / math.pi
    print(f"Ângulo em radianos: {r:.2f}")
    print(f"Ângulo em graus: {g:.2f}")
