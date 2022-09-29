'''
Escreva um algoritmo que lê um nome e uma idade
Caso o nome digitado seja Vinicius, escreva isso na tela
Caso o usuário digite qualquer outro nome, verifique sua idade. Se for menor que 18 anos, informe que é de menor. Se for maior que 100 anos, informe que esta pessoa possivelmente não existe
'''
nome = input('Digite o seu nome: ')
idade = int(input('Digite sua idade: '))

if (nome == 'Vinicius'):
    print(nome)
else:
    if (idade < 18):
        print('É de menor!')
    elif (idade > 100):
        print('Pessoa possivelmente não existe!')