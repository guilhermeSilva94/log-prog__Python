'''
Escreva um algoritmo que imprima na tela somente valores dentro de um intervalo especificado pelo usuário e que sejam números pares

'''

inicio = int(input('Por qual número irá iniciar: '))
fim = int(input('Por qual número irá encerrar: '))

x = inicio

if ( x%2 != 0):
    #x = x + 1
    x += 1
    
while(x <= fim):
    print(x)
    #x = x + 2
    x += 2


