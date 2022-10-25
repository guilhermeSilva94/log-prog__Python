'''
Escreva um algoritmo que leia dois valores numéricos e que pergunte ao usuário qual operação ele deseja realizar: adição (+),subtração (-), multiplicação (*), divisão (/) e sair. Exiba na tela o resultado da operação desejada.
Repita até que a opção saída seja escolhida
'''
while True:
    operacao = input('Qual operação você quer realizar? ')
    if (operacao == 'sair'):
        break
    v1 = int(input('Digite o primeiro valor: '))
    v2 = int(input('Digite o segundo valor: '))

    if (operacao == '+' or operacao == 'adição'):
        print(v1 + v2)
    elif (operacao == '-' or operacao == 'subtração'):
        print(v1 - v2)
    elif (operacao == '/' or operacao == 'divisão'):
        print(v1 / v2)
    elif (operacao == '*' or operacao == 'multiplicação'):
        print(v1 * v2)
print('Programa encerrado...')
