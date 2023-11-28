entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitda = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitda:
    print('Entrar')

else:
    print('Sair')