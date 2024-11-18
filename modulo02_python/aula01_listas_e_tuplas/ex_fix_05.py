# EXERCÍCIOS DE FIXAÇÃO

# 5 - Faça um programa que leia 5 números digitados pelo usuário e coloque-os em uma lista.
    # Imprima a lista no console.
    # Não crie 5 variáveis!

lista_usuario = []

for i in range(0, 5):
    num_usuario = int(input('Digite um número para adicioná-lo à lista: '))
    lista_usuario.append(num_usuario)

    tamanho = len(lista_usuario)
    
    if tamanho == 5:
        break

print(f'\n{lista_usuario}')
