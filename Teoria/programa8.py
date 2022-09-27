nota = 8.5
s1 = 'Você tirou %f na disciplina de Algoritmos' % nota
print(s1)

nota = 8.5
s1 = 'Você tirou %.2f na disciplina de Algoritmos' % nota
print(s1)

nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Você tirou %.2f na disciplina de %s' % (nota, disciplina)
print(s1)

nota = 8.5
disciplina = 'Algoritmos'
s1 = 'Você tirou {} na disciplina de {}' .format(nota, disciplina)
print(s1)