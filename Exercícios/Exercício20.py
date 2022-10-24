'''
Escreva um algoritmo que calcule a sua média de notas em determinada disciplina
Vamos assumir que a média final é dada pela média aritmética de cinco notas digitadas
'''

soma = 0
contador = 1
while (contador <= 5):
    x = float(input('Digite a {}ª nota: ' .format(contador)))
    soma += x #soma = soma + x
    contador += 1 #contador = contador + 1
media = soma / 5
print('Média final: {}'.format(media))