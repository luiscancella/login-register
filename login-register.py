from string import punctuation

def registrar():
    controle = True
    while controle:
        nome = input('Registre seu nome ---> ')
        controle1 = True
        try:
            test = open("banco.txt", "r")
            test.close()
        except FileNotFoundError:
            test = open("banco.txt", "w")
            test.close()
        with open("banco.txt", "r") as banco: #Verificação Usuário
            lines = banco.readlines()
            for dado in lines: 
                dado = dado.rstrip('\n')
                dado = dado.split('/')
                if dado[0] == nome:
                    print('Usuário já existe')
                    controle1 = False
        for letra in nome: #Verificação Caracteres
            if letra in punctuation:
                print('Não são premitidos caracteres especiais')
                controle1 = False
        if not 3 < len(nome) < 10: #Verificação len(nome)
            print('Nome muito grande ou pequeno(entre 4 e 9 caracteres)')
            controle1 = False
        while controle1:
            controle = False
            senha = input('Senha ---> ')
            if 5 < len(senha) < 10:
                controle1 = False
                with open("banco.txt", "a") as banco:
                    banco.write(f'{nome}/{senha}\n')
            else:
                print('Senha muito grande ou pequena(entre 6 e 9 caracteres)')

def logar():
    controle = True
    while controle:
        try:
            with open('banco.txt', 'r') as banco:
                nome = input('Seu nome --> ')
                lines = banco.readlines()
                for dado in lines:
                    login = dado.split('/')
                    loginnome = login[0].rstrip('\n')
                    loginsenha = login[1].rstrip('\n')
                    if loginnome == nome:
                        while True:
                            senha = input('Senha ---> ')
                            if senha == loginsenha:
                                print('Usuário logado')
                                return True
                            else:
                                print('Senha incorreta')
            print('Usuário inexistente, por favor insire um usuário válido')
        except FileNotFoundError:
            print("Dados não encontrados!")
            exit()

while True:
    escolha = int(input('O que deseja fazer?\n [1]Logar\n [2]Registrar\n [3]Sair\n--->'))
    if escolha == 1:
        logar()
        break
    elif escolha == 2:
        registrar()
    elif escolha == 3:
        print('Adeus')
        break
    else:
        print('Escolha algo')