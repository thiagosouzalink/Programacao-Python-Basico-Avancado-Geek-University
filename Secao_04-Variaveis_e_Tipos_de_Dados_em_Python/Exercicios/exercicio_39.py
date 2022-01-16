"""
39. A importância de R$ 780.000,00 será divida entre três ganhadores de
um concurso. Sendo que da quantia total:
    - O primeiro ganhador receberá 46%
    - O segundo receberá 32%
    - O terceiro ganhará o restante
Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""

TOTAL = 780000
PRIMEIRO_GANHADOR = TOTAL*0.46
SEGUNDO_GANHADOR = TOTAL*0.32
TERCEIRO_GANHADOR = TOTAL - PRIMEIRO_GANHADOR - SEGUNDO_GANHADOR

print(f"Premiação total: R$ {TOTAL:.2f}")
print(f"Valor do Primeiro Ganhador: R$ {PRIMEIRO_GANHADOR:.2f}")
print(f"Valor do Segundo Ganhador: R$ {SEGUNDO_GANHADOR:.2f}")
print(f"Valor do Terceiro Ganhador: R$ {TERCEIRO_GANHADOR:.2f}")
