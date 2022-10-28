#Listas

mochila = ('machado', 'camisa', 'bacon', 'abacate')
print('Tupla: ', mochila)
mochila = ['machado', 'camisa', 'bacon', 'abacate']
print('Lista: ', mochila)

mochila[2] = 'laranja'
print('Lista: ', mochila)

#Manipulando listas
mochila.append('ovos')
print('Lista: ', mochila)

mochila.insert(1, 'canivete')
print('Lista: ', mochila)

del mochila[1]
print('Lista: ', mochila)
mochila.remove('ovos')
print('Lista: ', mochila)


