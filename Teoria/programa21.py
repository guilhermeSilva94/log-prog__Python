'''
Escreva uma função para validar uma string.
Essa função recebe como parâmetro a string, o número mínimo e máximo de caracteres.
Retorne verdadeiro se o tamanho da string estiver entre os valore de mínimo e máximo, e falso, caso contrário (elaborado com base em Menezes, s. d.)
'''

string = input('Digite algo para validação: ')

def validacao(string, min, max):
    print(len(string))
    if(min > len(string) or max < len(string)):
        return False
    else:
        return True

teste = validacao(string, 5, 10)
print(teste)