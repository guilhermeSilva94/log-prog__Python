'''
Escreva um algoritmo que realize um login em um sistema
O usuário deve informar seu nome e senha
'''
while True:
    nome = input ('Qual o seu nome?')
    if (nome != 'Gui'):
        continue
    senha = input('Qual a sua senha?')
    if (senha == '333'):
        break
print('Acesso concedido.')