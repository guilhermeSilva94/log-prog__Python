'''
 Imagina-se que você é um dos programadores responsáveis pela construção de app de vendas para uma determinada empresa X que vende em atacado. Uma das estratégias de vendas dessa empresa X é dar descontos maiores por unidade conforme a tabela abaixo:

 Quandtidades                           Desconto
    Até 4                                   0% na unidade
    Entre 5 e 19                            3% na unidade
    Entre 20 e 99                           6% na unidade
    Maior ou igual a 100                    10% na unidade

Elabore um programa em Python que: 
    1. Entre com o valor unitário do produto(Lembra que número decimal é feito com ponto e não vírgula);
    2.Entre com a quantidade desse produto;
    3.O programa deve retornar o valor total sem desconto;
    4.O programa deve retornar o valor total após o desconto:
    5.Deve-se utilizar estruturas if, elif e else(EXIGÊNCIA 1 de 1);
    6.Colocar um exemplo de SAIDA DE CONSOLE de compra de mais de 10 unidades.

    Segue o exemplo de SAIDA DE CONSOLE:

    Bem vindo a loja do Guilherme Silva
    Entre com o valor do produto: 12.40
    Entre com o valor da quantidade: 10
    O valor sem desconto foi: R$ 124.00
    O valor com desconto foi: R$ 120.28 (desconto 3%)

'''

print('Bem vindo a loja do Guilherme Silva')

valor_produto = float(input('Entre com o valor do produto: '))

quantidade_produto = float(input('Entre com a quantidade de produtos: '))

total_sem_desconto = valor_produto * quantidade_produto

print('O valor total sem desconto é de: R$ {}' .format(total_sem_desconto))

if (quantidade_produto <= 4):
    print('Não há desconto comprando essa quantidade de produtos!')
elif (quantidade_produto <= 19):
    total_desconto = (total_sem_desconto/100) * 3
    print('O valor total com desconto é de: R$ {} (desconto de 3% = R$ {})' .format(total_sem_desconto - total_desconto, total_desconto))
elif (quantidade_produto <= 99):
    total_desconto = (total_sem_desconto/100) * 6
    print('O valor total com desconto é de: R$ {} (desconto de 6% = R$ {})' .format(total_sem_desconto - total_desconto, total_desconto))
else :
    total_desconto = (total_sem_desconto/100) * 10
    print('O valor total com desconto é de: R$ {} (desconto de 10% = R$ {})' .format(total_sem_desconto - total_desconto, total_desconto))