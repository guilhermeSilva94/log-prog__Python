'''
Escreva um algoritmo que calcule a média dos números pares de 1 até 100(1 e 100 inclusos).
Implemente o laço usando for
'''

soma = 0
quantidade = 0
for i in range(1,101,1):
    if(i % 2 == 0):
        soma += i
        quantidade += 1
media = soma / quantidade
print ('A média dos pares de 1 até 100 é: {}' .format(media))