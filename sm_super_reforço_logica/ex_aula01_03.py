limite_velocidade = 60
valor_base_multa = 20
valor_multa_por_kmh_excedido = 2
valor_final_multa = 0


velocidade_do_veiculo = int(input('\nDigite a velocidade do veículo: '))


if velocidade_do_veiculo > limite_velocidade * 1.1:
    km_velocidade_excedente = velocidade_do_veiculo - limite_velocidade
    valor_final_multa = valor_base_multa + (km_velocidade_excedente * valor_multa_por_kmh_excedido)

    print(f'\nVelocidade acima do permitido: {velocidade_do_veiculo} | Multa: {valor_final_multa}')

else:
    print(f'\nVelocidade permitida: {velocidade_do_veiculo}')
