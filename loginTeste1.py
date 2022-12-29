opcao1 = int(input('Digite 1 para realizar login e digite 2 para realizar cadastro: '))

login = {'giselle124': '12345610', 'danielD': 'acdgikoq'}

if (opcao1 == 1):
    a = str(input('Digite seu nome de usuario ou email: '))
    b = str(input('Digite sua senha: '))

    if a in login.keys() and b in login.values():
        print('Login efetuado com sucesso.')
    else:
        print('Nome de usuario ou senha invalidos.')
if (opcao1 == 2):
    print('Preencha as informações abaixo para realizar seu cadastro.')
    email = str(input('informe o seu email ou nome de usuário: '))
    senha = str(input('informe a sua senha: '))

    login[email] = senha

    print('Cadastro finalizado')

    opcao2 = int(input('Digite 3 para realizar login: '))

    if (opcao2 == 3):

        c = str(input('Digite seu nome de usuario ou email: '))
        d = str(input('Digite sua senha: '))

        if c in login.keys() and d in login.values():
            print('Login efetuado com sucesso.')
        else:
            print('Nome de usuario ou senha invalidos.')
