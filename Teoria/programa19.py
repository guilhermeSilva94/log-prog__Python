def realce(s1):
    print('|','__' * 10, '|')
    print('|','__' * 10, '|')
    print('         ' + s1)
    print('|','__' * 10, '|')
    print('|','__' * 10, '|')

realce('MENU')

print('-' * 50)

def sub2(x,y):
    res = x - y
    print(res)

sub2(5, 7)

print('-' * 50)

def soma3 (x = 0,y = 0,z = 0):
    res = x + y + z
    print(res)

soma3(1,2,3)
soma3(1,2)
soma3(1)
soma3()