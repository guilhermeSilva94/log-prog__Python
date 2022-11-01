# Função Metragem Limpeza
def metragem_limpeza():
    print('-' * 28 + ' Menu 1 de 3 - Metragem Limpeza ' + '-' * 28)
    while True:
        try:
            metragem = float(input('Entre com a metragem da casa: '))
            if (metragem < 30 or metragem > 700):
                print('!! Não aceitamos casas com metragem menor que 30m² ou maior que 700m² !!')
            elif (metragem >= 30 and metragem < 300):
                return 60 + 0.3 * metragem
                break
            elif (metragem >= 300 and metragem < 700):
                return 120 + 0.5 * metragem
                break
        except ValueError:
            print('Digite um valor númerico no campo da metragem')

# Função Tipo de Limpeza
def tipo_limpeza():
    print('-' * 28 + ' Menu 2 de 3 - Tipo de Limpeza ' + '-' * 29)
    print('Tipos de limpeza:')
    print('B - Básica - Indicada para sujeiras semanais ou quinzenais')
    print('C - Completa - (30% a mais no valor) - Indicada para sujeiras antigas e/ou não rotineiras')
    while True:
        tipo = input('Entre com o tipo de limpeza: ')
        if (tipo == 'B'):
            print('Você selecionou a limpeza BÁSICA')
            return 1
            break
        elif (tipo == 'C'):
            print('Você selecionou a limpeza COMPLETA')
            return 1.30
            break
        else: 
            print('!!! Opção Inválida !!!')

# Função Adicional de Limpeza
def adicional_limpeza():
    print('-' * 28 + ' Menu 3 de 3 - Adicional de Limpeza ' + '-' * 24)
    print('Deseja mais algum adicional?')
    print('0- Não desejo mais nada(encerrar)')
    print('1- Passar 10 peças de roupas - R$ 10,00')
    print('2- Limpeza de 1 Forno/Micro-ondas - R$ 12,00')
    print('3- Limpeza de 1 Geladeira/Freezer - R$ 20,00')

    # Variável para somar valores dos serviços adicionais
    soma = 0
    while True:
        adicionais = int(input('Escolha o adicional ou digite 0 para encerrar: '))
        if (adicionais == 0):
            break
        elif (adicionais == 1):
            soma += 10.00
            print('>>>1')
        elif (adicionais == 2):
            soma += 12.00
            print('>>>2')
        elif (adicionais == 3):
            soma += 20.00
            print('>>>3')
        else:
            print('!!! Opção Inválida !!!')
    return soma

# Programa Principal

# Identificação
print('Bem-vindo ao Programa de Serviços de Limpeza do Guilherme dos Santos Silva - RU: 4059100')
print('*' * 88)

# Chamada da função metragem_limpeza e armazenamento do valor cobrado por metragem
valor_metragem =  metragem_limpeza()
print('O valor cobrado por essa metragem é de R$ {}' .format(valor_metragem))
print('*' * 88)

# Chamada da função tipo_limpeza e armazenamento do multiplicador no caso da limpeza completa
tipo = tipo_limpeza()
print('*' * 88)

# Chamada da função adicional_limpeza e armazenamento dos valores dos adicionais escolhidos
adicionais = adicional_limpeza()
print('*' * 88)

# Soma do valor total da limpeza
print('TOTAL: R$ {} (metragem: {} * tipo: {} + adicionais: {})' .format(valor_metragem * tipo + adicionais, valor_metragem, tipo, adicionais))