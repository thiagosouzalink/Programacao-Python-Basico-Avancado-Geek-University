"""
38. Leia o salário de um funcionário. Calcule e imprima o valor do novo
salário, sabendo que ele recebeu um aumento de 25%
"""

try:
    salario = float(input("Digite o salário do funcionário: "))
except ValueError:
    print("O valor deve ser um número inteiro ou decimal.")
else:
    AUMENTO = 0.25
    novo_salario = salario + salario*AUMENTO
    print(f"Salario Atual: R$ {salario:.2f}")
    print(f"Aumento: {int(AUMENTO*100)}%")
    print(f"Novo salário: R$ {novo_salario:.2f}")
