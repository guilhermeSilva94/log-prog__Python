'''
Escreva um algoritmo em Python que calcule a tabuada de todos os números de 1 até 10, e, para cada número, vamos calcular a tabuada multiplicando-o pelo intervalo de 1 até 10
'''

'''
2While
tabuada = 1
while (tabuada <= 10):
    print('TABUADA DO {}:' .format(tabuada))
    i = 1
    while (i <= 10):
        print('{} x {} = {}' . format(tabuada, i, tabuada * i))
        i += 1
    tabuada += 1

2FOR
for tabuada in range(1,11,1):
    print('TABUADA DO {}:' .format(tabuada))
    for i in range(1,11,1):
        print('{} x {} = {}' . format(tabuada, i, tabuada * i))'''

#1FOR e 1While
tabuada = 1
while (tabuada <= 10):
    print('TABUADA DO {}:' .format(tabuada))
    for i in range(1,11,1):
        print('{} x {} = {}' . format(tabuada, i, tabuada * i))
    tabuada += 1