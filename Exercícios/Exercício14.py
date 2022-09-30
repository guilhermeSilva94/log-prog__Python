'''
Traduza as afirmações a seguir para condicionais em Python:
    a)Se idade é maior que 60, escreva: "Você tem direitos aos benefícios"
    b)Se dano é maior do que 10 e escudo é igual a 0, escreva: "Você está morto!"
    c)Se pelo menos uma das variáveis booleanas norte, sul, leste e oeste resutarem em True, escreva: "Você escapou!"
'''

idade = 61 #int(input('Digite a idade: '))

if(idade > 60):
    print('Você tem direito aos benefícios')



dano = 11 #int(input('Digite o valor do dano: '))
escudo = 0 #int(input('Digite o valor do escudo: '))

if(dano > 10 and escudo == 0):
    print('Você está morto!')


norte = True
sul = False
leste = False
oeste = False

if ((norte == True) or (sul == True) or (leste == True) or (oeste == True) ):
    print('Você escapou!')