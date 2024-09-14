Estudantes = 1
Disciplinas = 2
Professores = 3
Turmas = 4
Matriculas = 5

op1 = 1
op2 = 2
op3 = 3
op4 = 4
op5 = 5

menuPrincipal: str = "Menu principal: 1. Estudantes, 2. Disciplinas, 3. Professores, 4. Turmas, 5. Matrículas, 6. Sair"
menuDeOperacoes: str  = "Menu de operações: 1. Incluir 2. Listar 3. Atualizar 4. Exluir 5. Voltar ao menu principal"

print("Olá! Seja bem vindo ao sistema de gestão de dados")

while True:

    print(menuPrincipal)

    inputUser = int(input("Escolha qual opção deseja acessar:"))

    if inputUser == 1:
        print("A opção escolhida foi: Opção 1. Estudantes")
    elif inputUser == 2:
        print("A opção escolhida foi: Disciplinas.")
    elif inputUser == 3:
        print("A opção escolhida foi: Professores.")
    elif inputUser == 4:
        print("A opção escolhida foi: Turmas.")
    elif inputUser == 5:
        print("A opção escolhida foi: Matrículas.")
    elif inputUser == 6:
        print("Saindo do sistema")
        break
    else:
        print("Opção inválida, escolha novamente.")
        continue
    break

while True:

    print(menuDeOperacoes)

    inputOperacao = int(input("Escolha qual opção deseja acessar:"))

    if inputOperacao == 1:
        print("Opção 1: Incluir")
        continue
    elif inputOperacao == 2:
        print("Opção 2: Listar")
        continue
    elif inputOperacao == 3:
        print("Opção 3: Atualizar")
        continue
    elif inputOperacao == 4:
        print("Opção 4: Excluir")
        continue
    else:
        if inputOperacao == 5:
            print("Voltar ao menu principal")

        print(menuPrincipal)
        inputUser = int(input("Escolha qual opção deseja acessar:"))

        if inputUser == 1:
            print("A opção escolhida foi: Opção 1. Estudantes")
        elif inputUser == 2:
            print("A opção escolhida foi: Disciplinas.")
        elif inputUser == 3:
            print("A opção escolhida foi: Professores.")
        elif inputUser == 4:
            print("A opção escolhida foi: Turmas.")
        elif inputUser == 5:
            print("A opção escolhida foi: Matrículas.")
        elif inputUser == 6:
            print("Saindo do sistema")
            break
        else:
            print("Opção inválida, digite novamente.")
        continue

print("Fim da aplicação.")

