'''
Expressões booleanas
    Escreva as seguintes expressões booleanas em linguagem Python:
        a) O somatório de 2 com 2 é menor do que 4
        b) O valor 7 // 3 é igual a 1 + 1
        c) A soma de 3 elevado ao quadrado com 4 elevado ao quadrado é igual a 25
        d) A soma de 2, 4 e 6 é maior do que 12
        e)1387 é divisível por 19
        f)31 é par
        g)O menor valor entre: 34, 29 e 31 é menor do que 30
'''

a = 2 + 2 < 4
print(a)

b = (7 // 3) == (1 + 1)
print(b)

c = (3 ** 2) + (4 ** 2) == 25
print(c)

d = (2 + 4 + 6) > 12
print(d)

e = 1389 % 19 == 0
print(e)

f = 31 % 2 == 0
print(f)

g = min(34, 29 , 31) < 30
print(g)