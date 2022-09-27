'''
Crie uma varável de string que receba uma frase qualquer. Crie uma segunda variável, agora contendo a metade da string digitada.
Imprima na tela somente os dois últimos caracters da segunda variável do tipo string
'''

frase1 = input('Digite uma frase: ')
tamanho = len(frase1)

frase2 = frase1[:int(tamanho/2)]

print(frase2[-2:])