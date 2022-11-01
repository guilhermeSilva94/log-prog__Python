# Variáveis globais
lista_funcionarios = []
codigo_funcionario = 0
  
# Função cadastrar funcionário
def cadastrar_funcionario(id):
    print('*' * 90)
    print('-' * 40 +' MENU CADASTRAR FUNCIONÁRIO ' + '-' * 22)
    nome = input('Entre com o nome: ')
    setor = input('Entre com o setor: ')
    salario = float(input('Entre com o salário (R$): '))
    dicionario_funcionarios = { 'codigo'  : id,
                                'nome'    : nome,
                                'setor'   : setor,
                                'salario' : salario}
    lista_funcionarios.append(dicionario_funcionarios.copy())
# Fim função cadastrar funcionário

# Função consultar funcionários
def consultar_funcionarios():
    print('*' * 90)
    print('-' * 40 +' MENU CONSULTAR FUNCIONÁRIOS ' + '-' * 21)
    while True:
        consulta = input('Escolha a opção desejada:\n'+
                    '1-Consultar Todos os Funcionários\n'+
                    '2-Consultar Funcionários por ID\n'+
                    '3-Consultar Funcionários por SETOR\n'+
                    '4-Retornar\n'+
                    '>>>')
        if consulta == '1':
            print('*' * 90)
            print('TODOS FUNCIONÁRIOS')
            for funcionario in lista_funcionarios:
                print('*' * 90)
                for key, value in funcionario.items():
                    print('{}: {}'.format(key,value))
                print('*' * 90)
        elif consulta == '2':
            print('CONSULTA POR ID')
            entrada_codigo = int(input('Entre com o ID do funcionário: '))
            print('*' * 90)
            for funcionario in lista_funcionarios:
                if funcionario['codigo'] == entrada_codigo:
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key,value))
                    print('*' * 90)
        elif consulta == '3':
            print('CONSULTA POR SETOR')
            entrada_setor = input('Entre com o setor do funcionário: ')
            print('*' * 90)
            for funcionario in lista_funcionarios:
                if funcionario['setor'] == entrada_setor:
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key,value))
                    print('*' * 90)
        elif consulta == '4':
            return
        else:
            print('!!! OPÇÃO INVÁLIDA !!!')
            print('*' * 90)
            continue
# Fim função consultar funcionários

# Função remover funcionário
def remover_funcionario():
    print('*' * 90)
    print('-' * 40 +' MENU REMOVER FUNCIONÁRIO ' + '-' * 24)
    entrada_codigo = int(input('Entre com o ID do funcionário: '))
    for funcionario in lista_funcionarios:
        print('*' * 90)
        if funcionario['codigo'] == entrada_codigo:
            lista_funcionarios.remove(funcionario)
            print('Funcionário removido!!!')
            print('*' * 90)
# Fim função remover funcionário

# Programa Principal

# Identificação
print('Bem-vindo ao Controle de Funcionários do Guilherme dos Santos Silva - RU: 4059100')
print('*' * 90)

# Menu principal
while True:
    print('-' * 40 +' MENU PRINCIPAL ' + '-' * 34)
    opcao = input('Escolha a opção desejada:\n'+
                '1-Cadastrar Funcionário\n'+
                '2-Consultar Funcionário(s)\n'+
                '3-Remover Funcionário\n'+
                '4-Sair\n'+
                '>>>')
    if opcao == '1':
        codigo_funcionario += 1
        cadastrar_funcionario(codigo_funcionario)
    elif opcao == '2':
        consultar_funcionarios()
    elif opcao == '3':
        remover_funcionario()
    elif opcao == '4':
        break
    else:
        print('!!! OPÇÃO INVÁLIDA !!!')
        print('*' * 90)
        continue
# Fim menu principal