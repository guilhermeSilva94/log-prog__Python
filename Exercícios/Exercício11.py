'''
Escreva um algoritmo em Python em que o usuário escolhe se quer comprar maçãs, laranjas ou bananas. Deverá ser apresentado na tela um menu com as opções: 1 para maçã, 2 para laranja e 3 para banana
Após escolhida a fruta, deve-se digitar quantas unidades se que comprar. O algoritmo deve calcular o preço total a pagar do produto escolhido e mostrá-lo na tela
Considere que uma maçã custa R$ 2.30, uma laranja custa R$ 3.60 e uma banana custa R$ 1.85
'''


print('1 = maçã - 2 = laranja - 3 = banana')

frutaEscolhida = int(input('Digite o número correspondente da fruta desejada: '))
quantidade = int(input('Digite quantas unidade você quer comprar: '))

if(frutaEscolhida == 1):
    precoTotal = quantidade * 2.30
    print('O preço total a pagar é R$ {}'.format(precoTotal))
else:
    if(frutaEscolhida == 2):
        precoTotal = quantidade * 3.60
        print('O preço total a pagar é R$ {}'.format(precoTotal))
    else:
        if(frutaEscolhida == 3):
            precoTotal = quantidade * 1.85
            print('O preço total a pagar é R$ {}'.format(precoTotal))
        else:
            print('Produto inexistente!')
'''
if (frutaEscolhida == 1):
        precoTotal = quantidade * 2.30
        print('O preço total a pagar é R$ {}'.format(precoTotal))
elif (frutaEscolhida == 2):
        precoTotal = quantidade * 3.60
        print('O preço total a pagar é R$ {}'.format(precoTotal))
elif (frutaEscolhida == 3):
        precoTotal = quantidade * 1.85
        print('O preço total a pagar é R$ {}'.format(precoTotal))
else:
        print('Produto inexistente!')
'''



