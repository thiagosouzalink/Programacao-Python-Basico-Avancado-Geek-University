"""
34. Leia o valor do raio de um círculo e calcule e imprima a área do
círculo correspondente. A área do círculo é PI * raio², considere
PI = 3.141592
"""

try:
    raio = float(input("Digite o valor do raio do círculo: "))
except ValueError:
    print("O valor deve ser um número inteiro ou decimal.")
else:
    PI = 3.141592
    area = PI * raio * raio
    print(f"Raio: {raio}")
    print(f"Área do círculo: {area:.2f}")
