"""
30. Leia um valor em real e a cotação do dólar. em seguida, imprima o
valor correspondente em dólares.
"""

try:
    real = float(input("Digite o valor em Real: "))
    cotacao_dolar = float(input("Digite a cotação do dólar: "))
except ValueError:
    print("O valor deve ser um número inteiro ou fracional.")
else:
    dolar = real * cotacao_dolar
    print(f"Valor em Real: R$ {real:.2f}")
    print(f"Valor em Dólar: US$ {dolar:.2f}")
