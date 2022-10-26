'''
Escreva uma rotina que crie uma borda ao redor de uma palavra para destcála como parâmetro a palavra a ser destacada. O tamanho da caixa de texto deverá ser adaptável de acordo com o tamanho da palavra.
'''


def borda(palavra):
    tamanho = len(palavra)
    if tamanho:
        print('+' + '-' * tamanho + '+')
        print('|' + palavra + '|')
        print('+' + '-' * tamanho + '+')

borda ('Guilherme')