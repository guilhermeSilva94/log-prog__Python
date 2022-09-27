'''
Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$0,15 por km rodado.
'''

diaria = 60
valorKm= 0.15

kmPercorridos = float(input('Quantos Km foram percorridos?'))
diasAlugados = float(input('Quantos dias ficaram com o carro?'))

valor = (kmPercorridos * valorKm) + (diasAlugados * diaria)

print('o valor total a pagar é R$ {} reais' .format(valor))