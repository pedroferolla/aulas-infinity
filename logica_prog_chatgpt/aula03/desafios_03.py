# DESAFIOS

# 3 - Escreva um programa que calcule o montante final após N anos de um investimento inicial P,
    # com uma taxa de juros anual fornecida pelo usuário.
    # Use um loop For para calcular os juros compostos.

# RESULTADO ESPERADO:
    # Digite o valor do investimento inicial (P): 1000
    # Digite a taxa de juros anual (%): 5
    # Digite o número de anos (N): 10
    # ------------------------------------------------
    # Após 10 anos, com um investimento inicial de R$ 1000.00 e uma taxa de juros anual de 5.00%:
    # O montante final é de R$ 1628.89

pv = float(input('Digite o valor do investimento inicial (P): '))
i = float(input('Digite a taxa de juros anual (%): '))
n = int(input('Digite o número de anos (N): '))
n_inicial = 0
i_percentual = i / 100

pmt = i_percentual * pv
# fv = pv + pmt   <--------- O fv deve se iniciar com o mesmo valor de pv!
fv = pv


while n_inicial < n:
    n_inicial += 1
    pmt = i_percentual * fv
    fv += pmt

    if n_inicial == n:
        break

print(f'\nApós {n} anos, com um investimento inicial de R$ {pv:.2f} e uma taxa de juros anual de {i}%:')
print(f'O montante final é de R$ {fv:.2f}')
