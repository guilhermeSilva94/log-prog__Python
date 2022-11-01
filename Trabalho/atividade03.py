# Identificação
print('Bem-vindo a Sorveteria do Guilherme dos Santos Silva - RU: 4059100')

# Tabela da sorveteria
print('-' * 44 + 'Cardápio' + '-' * 45)
print('| Código | Descrição            | Tamanho P (500 ml) | Tamanho M (1000 ml) | Tamanho G(2000 ml) |')
print('|   TR   | Sabores Tradicionais |     R$ 6,00        |        R$ 10,00     |       R$ 18,00     |')
print('|   ES   | Sabores Especiais    |     R$ 7,00        |        R$ 12,00     |       R$ 21,00     |')
print('|   PR   | Sabores Premium      |     R$ 8,00        |        R$ 14,00     |       R$ 24,00     |')
print('-' * 97)

# Variável para acumular valor no caso de mais de um pedido 
soma = 0

# Repetidor para execução dos pedidos
while True:

    # Variáveis de entrada
    tamanho = input('Entre com o Tamanho do pote desejado (P/M/G): ')
    codigo = input('Entre com o código do sabor desejado (TR/ES/PR): ')
    
    # Verificadores da escolha do sabor e tamanho do sorvete
    if (codigo == 'TR' and tamanho == 'P'):
        soma += 6.00
        print('Você pediu um sorvete sabor TRADICIONAL {} de R$ 6,00' .format(tamanho))
    elif (codigo == 'TR' and tamanho == 'M'):
        soma += 10.00
        print('Você pediu um sorvete sabor TRADICIONAL {} de R$ 10,00' .format(tamanho))
    elif (codigo == 'TR' and tamanho == 'G'):
        soma += 18.00
        print('Você pediu um sorvete sabor TRADICIONAL {} de R$ 18,00' .format(tamanho))
    elif (codigo == 'ES' and tamanho == 'P'):
        soma += 7.00
        print('Você pediu um sorvete sabor ESPECIAL {} de R$ 7,00' .format(tamanho))
    elif (codigo == 'ES' and tamanho == 'M'):
        soma += 12.00
        print('Você pediu um sorvete sabor ESPECIAL {} de R$ 12,00' .format(tamanho))
    elif (codigo == 'ES' and tamanho == 'G'):
        soma += 21.00
        print('Você pediu um sorvete sabor ESPECIAL {} de R$ 21,00' .format(tamanho))
    elif (codigo == 'PR' and tamanho == 'P'):
        soma += 8.00
        print('Você pediu um sorvete sabor PREMIUM {} de R$ 8,00' .format(tamanho))
    elif (codigo == 'PR' and tamanho == 'M'):
        soma += 14.00
        print('Você pediu um sorvete sabor PREMIUM {} de R$ 14,00' .format(tamanho))
    elif (codigo == 'PR' and tamanho == 'G'):
        soma += 24.00
        print('Você pediu um sorvete sabor PREMIUM {} de R$ 24,00' .format(tamanho))

    # Verificador de erro na hora da escolha
    else:
        print('[ERRO] TAMANHO OU CÓDIGO INVÁLIDO(S)')
        continue
    
    # Variável e verificador  para continuar ou encerrar o pedido
    novo_pedido = input('Deseja pedir mais alguma coisa? (S/N)')
    if (novo_pedido == 'N'):
        break

# Valor total do pedido
print('O total a ser pago é: R$ {}'.format(soma))