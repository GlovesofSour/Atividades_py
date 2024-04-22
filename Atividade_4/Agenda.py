agenda = {}

def adiciona(agenda):
        nome = input("Nome: ")
        aniversario = input("Data de aniversário: ")
        email = input("Email: ")
        telefone = input("Telefone: ")
        agenda[nome] = {'aniversario': aniversario, 'email': email, 'telefone': telefone}

def apaga(agenda):
    nome = input("Digite o nome da pessoa que deseja apagar: ")
    if nome in agenda:
        del agenda[nome]
        print("Contato apagado com sucesso.")
    else:
        print("Contato não encontrado na agenda.")

def altera(agenda):
    nome = input("Digite o nome da pessoa que deseja alterar: ")
    if nome in agenda:
        novo_nome = input("Novo nome: ")
        novo_aniversario = input("Nova data de aniversário: ")
        novo_email = input("Novo email: ")
        novo_telefone = input("Novo telefone: ")
        agenda[novo_nome] = {'aniversario': novo_aniversario, 'email': novo_email, 'telefone': novo_telefone}
        if novo_nome != nome:
            del agenda[nome]
        print("Contato alterado com sucesso.")
    else:
        print("Contato não encontrado na agenda.")

def lista_nomes(agenda):
    if not agenda:
        print("Agenda vazia.")
    else:
        print("Lista de contatos:")
        for i, nome in enumerate(agenda.keys(), 1):
            print(f"{i}. {nome}")

def busca(agenda):
    nome = input("Digite o nome da pessoa que deseja buscar: ")
    if nome in agenda:
        print("Informações do contato:")
        print(f"Nome: {nome}")
        print(f"Aniversário: {agenda[nome]['aniversario']}")
        print(f"Email: {agenda[nome]['email']}")
        print(f"Telefone: {agenda[nome]['telefone']}")
    else:
        print("Contato não encontrado na agenda.")

def grava(agenda):
    arquivo = open("agenda.txt", "w")
    for nome, dados in agenda.items():
        arquivo.write(f"{nome},{dados['aniversario']},{dados['email']},{dados['telefone']}\n")
    arquivo.close()
    print("Agenda gravada com sucesso.")

def menu(agenda):
    while True:
        print("\n======= Menu =======")
        print("1 - Adicionar contato")
        print("2 - Apagar contato")
        print("3 - Alterar contato")
        print("4 - Listar contatos")
        print("5 - Buscar contato")
        print("6 - Gravar agenda")
        print("7 - Exibir tamanho da agenda")
        print("8 - Ordenar lista por nome")
        print("0 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            adiciona(agenda)
        elif opcao == 2:
            apaga(agenda)
        elif opcao == 3:
            altera(agenda)
        elif opcao == 4:
            lista_nomes(agenda)
        elif opcao == 5:
            busca(agenda)
        elif opcao == 6:
            grava(agenda)
        elif opcao == 7:
            print(f"Tamanho da agenda: {len(agenda)} contatos.")
        elif opcao == 8:
            agenda = dict(sorted(agenda.items()))
            print("Agenda ordenada por nome.")
        elif opcao == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu(agenda)