'''
Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário. Verifique se os valores formam um triângulo e classifique como:
a)Equilátero(três lados iguais)
b)Isósceles(dois lados iguais)
c)Escaleno(três lados diferentes)
Lembre-se de que, para formar um triângulo, nenhum dos lados pode ser igual a zero, e um lado não pode ser maior do que a soma dos outros dois
'''

ladoA = int(input('Informe o valor do lado A: '))
ladoB = int(input('Informe o valor do lado B: '))
ladoC = int(input('Informe o valor do lado C: '))


if (ladoA == 0 or ladoB == 0 or ladoC == 0):
    print('Não é possível formar um triângulo')
elif (ladoA + ladoB < ladoC or ladoA + ladoC < ladoB or ladoB + ladoC < ladoA):
    print('Não é possível formar um triângulo')
elif (ladoA == ladoB and ladoA == ladoC):
    print('Triângulo Equilátero')
elif (ladoA != ladoB and ladoA != ladoC and ladoB != ladoC):
    print('Triângulo Escaleno')
else:
    print('Triângulo Isósceles')