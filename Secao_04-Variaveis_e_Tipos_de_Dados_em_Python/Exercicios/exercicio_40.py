"""
40. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um
programa que solicite o número de dias trabalhados pelo encanador e
imprima a quantia líquida que deveá ser paga, sabendo-se que são
descontados 8% para o imposto de renda.
"""

try:
    dias = int(input("Digite o número de dias trabalhados pelo encanador: "))
except ValueError:
    print("O valor deve ser um número inteiro.")
else:
    VALOR_DIA = 30
    IMPOSTO = 0.08
    quantia_bruta = dias * VALOR_DIA
    quantia_liquida = quantia_bruta - quantia_bruta*IMPOSTO
    print(f"Dias Trabalhados: {dias}")
    print(f"Valor Salário Diário: R$ {VALOR_DIA:.2f}")
    print(f"Valor Salário Bruto: R$ {quantia_bruta:.2f}")
    print(f"Imposto de Renda: {int(IMPOSTO*100)}%")
    print(f"Salário Líquido a Receber: R$ {quantia_liquida:.2f}")
