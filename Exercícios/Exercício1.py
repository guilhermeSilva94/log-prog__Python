'''Desenvolva um algoritmo que solicite ao usuário dois números inteiros. Imprima a soma destes dois números na tela'''



n1 = int(input('Digite o primeiro número'))
n2 = int(input('Digite o segundo número'))

resposta = 'O resultado da soma de %i com %i é %i' %(n1, n2, n1 + n2)
print(resposta)

resposta = 'O resultado da soma de {} com {} é {}' .format(n1, n2, n1 + n2)
print(resposta)


