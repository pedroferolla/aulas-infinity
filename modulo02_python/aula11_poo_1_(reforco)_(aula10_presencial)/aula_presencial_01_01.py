def depositar(valor_a_depositar: float, saldo_inicial: float):
    saldo_final = valor_a_depositar + saldo_inicial
    return saldo_final

saldo = 0
print(f'Valor antes do depósito: {saldo}')

saldo = depositar(1000, saldo)
print(f'Valor depois do depósito: {saldo}')
