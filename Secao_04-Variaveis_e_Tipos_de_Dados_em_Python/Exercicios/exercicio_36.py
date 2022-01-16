"""
36. Leia a altura e o raio de um cilindro circular e imroima o volume do
cilindro. O volulme de um cilindro circular é calculado por meio da
seguinte fórmula: V = PI * raio² * altura, onde PI = 3,141592
"""

try:
    altura = float(input("Digite o valor da altura do cilindro: "))
    raio = float(input("Digite o valor do raio do cilindro: "))
except ValueError:
    print("O valor deve ser um número inteiro ou decimal.")
else:
    PI = 3.141592
    volume = PI * raio**2 * altura
    print(f"Altura do cilindro: {altura}")
    print(f"Raio do cilindro: {raio}")
    print(f"Volume do cilindro: {volume:.2f}")
