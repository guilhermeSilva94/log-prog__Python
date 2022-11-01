# Identificação
print('Bem-vindo a Loja do Guilherme dos Santos Silva - RU: 4059100')

# Variáveis de registro de valor e quantidade de produto
valor = float(input('Entre com o valor do produto: '))
quantidade = int(input('Entre com a quantidade de produto: '))

# Variável para calcular valor total sem frete
valor_sem_frete = valor * quantidade
print('O valor sem frete é: R$ {}'.format(valor_sem_frete))

# Condições para se calcular valor com frete
if quantidade < 11:
    frete = 30.00
elif quantidade < 101:
    frete = 60.00
elif quantidade < 1001:
    frete = 120.00
else:
    frete = 240.00

# Retorno do valor com frete
print('O valor com frete é: R$ {} (frete de R$ {})' .format(valor_sem_frete + frete, frete))