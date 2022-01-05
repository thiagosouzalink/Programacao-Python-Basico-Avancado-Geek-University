"""
28. Faça uma leitura de três valores e apresente como resultado a soma
dos quadrados dos três valores lidos.
"""

try:
    num1 = float(input("Digite o valor do primeiro número: "))
    num2 = float(input("Digite o valor do segundo número: "))
    num3 = float(input("Digite o valor do terceiro número: "))
except ValueError:
    print("O valor deve ser um número inteiro ou fracional.")
else:
    soma = num1**2 + num2**2 + num3**2
    print(f"A soma dos quadrados dos números {num1:.2f}, {num2:.2f} e "
          f"{num3:.2f} é: {soma:.2f}")
