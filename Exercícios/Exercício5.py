'''
Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele.
Calcule e exiba o valor do desconto e o preço final do produto
'''

preco = float(input('Qual o preço do produto?'))
desconto = float(input('Qual é o percentual de desconto do produto(0-100)?'))

valorDesconto = (preco/100) * desconto
valorFinal = preco - valorDesconto

print('O valor do desconto é {} reais. E o valor final do produto é {} reais.' .format(valorDesconto, valorFinal))