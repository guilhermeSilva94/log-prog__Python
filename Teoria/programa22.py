#Construindo e manipulando tuplas

mochila = ('machado', 'camisa', 'bacon', 'abacate')
print(mochila)

print(mochila[0])
print(mochila[2])
print(mochila[0:2])
print(mochila[2:])
print(mochila[-1])
 

for item in mochila:
    print('Na minha mochila tem: {}' .format(item))


tam = len(mochila)
for i in range (0, tam, 1):
        print('Na minha mochila tem: {}' .format(mochila[i]))


