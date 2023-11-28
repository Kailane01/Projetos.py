nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontar: ')

if encontrar in nome:
    print(f'{encontrar} está com {nome}')

else:
    print(f'{encontrar} não está com {nome}')
