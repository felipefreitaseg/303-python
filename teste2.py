# import math

# exponencial = math.exp(3)

# print(exponencial)
def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    dinheiro = float(valor_hora)
    if horas >= 40:
        salario = horas * dinheiro
        print("Voce receberá RS", salario)
    else:
        salario = 0
        print("vc nao trabalhou o suficiente")
    return salario

calcular_pagamento(40,20)
