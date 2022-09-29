'''
Um aluno, para passar de ano, precisa ser aprovado em todas as matérias que está cursando
Assuma que a média para aprovação é a partir de 7, e que o aluno cursa 3 matérias, somente. Escreva um algoritmo que leia a nota final do aluno e em cada matéria e informe, na tela, se ele passou de ano ou não.
'''

materia1 = float(input('Digite a nota da primeira matéria: '))
materia2 = float(input('Digite a nota da segunda matéria: '))
materia3 = float(input('Digite a nota da terceira matéria: '))


if(materia1 >= 7 and materia2 >= 7 and materia3 >= 7):
    print('O aluno passou de ano!')
else:
    print('O aluno reprovou!')