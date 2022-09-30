'''
Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios
Calcule o preço de acordo com os valores a seguir:
Residencial:
    Até 500 = 0.40
    Acima de 500 = 0.65
Comercial:
    Até 1000 = 0.55
    Acima de 1000 = 0.60
Industrial
    Até 5000 = 0.55
    Acima de 5000 = 0.60
'''

consumo = float(input('Digite a quantidade de kWh consumida: '))
instalacao = input('Digite o tipo de instalação: ')

if (instalacao == 'R'):
    if (consumo <= 500):
        print(consumo * 0.40)
    else:
        print(consumo * 0.65)

elif (instalacao == 'C'):
    if (consumo <= 1000):
        print(consumo * 0.55)
    else:
        print(consumo * 0.60)
        
elif (instalacao == 'I'):
    if (consumo <= 5000):
        print(consumo * 0.55)
    else:
        print(consumo * 0.60)