#Dicionários

game = {'nome': 'Super Mario', 
        'desenvolvedora' : 
        'Nintendo', 'ano' : 1990}
print(game)

print(game['nome'])
print(game['desenvolvedora'])
print(game['ano'])

print(game.values())
print(game.keys())
print(game.items())

for i in game.values():
    print(i)

for i in game.keys():
    print(i)

for i in game.items():
    print(i)

for i,j in game.items():
    print('{} = {}'.format(i, j))