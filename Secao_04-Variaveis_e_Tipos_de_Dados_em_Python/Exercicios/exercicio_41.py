"""
41. Faça um programa que leia o valor da hora de trabalho (em reais) e
número de horas trabalhadas no mês. Imprima o valor a ser pago ao
funcionário, adicionando 10 % sobre o valor calculado.
"""

try:
    valor_hora = float(input("Digite o valor da hora de trabalho: R$ "))
    horas_trabalhadas = int(input("Digite o total de horas trabalhadas: "))
except ValueError:
    print("O valor informado não é permitido.")
else:
    valor_total = valor_hora * horas_trabalhadas
    ACRESCIMO = 0.1
    valor_final = valor_total + valor_total*ACRESCIMO
    print(f"Valor por hora: R$ {valor_hora:.2f}")
    print(f"Horas trabalhadas: {horas_trabalhadas}")
    print(f"Salario a receber: R$ {valor_total:.2f}")
    print(f"Acréscimo ao Salário: {ACRESCIMO*100}%")
    print(f"Salario final a receber: R$ {valor_final:.2f}")
