'''
Realize a sequência de print com for e while:
    a. Inteiros de 3 até, com 12 incluso
    b. Inteiros de 0 até 9, excluindo 9, com passo de 2
'''
#a
for i in range(3,13,1):
    print(i)

x = 3 
while x <= 12:
    print(x)
    x += 1

#b
for i in range(0,9,2):
    print(i)

x = 0
while x <= 9:
    print(x)
    x += 2