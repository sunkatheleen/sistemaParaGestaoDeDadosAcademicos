print("Olá!Seja bem vindo ao menu principal")

menuPrincipal = int(input(f"Escolha qual opção deseja acessar: 1. Estudantes, 2. Disciplinas, 3. Professores, 4. Turmas, 5. Matrículas, 6. Sair"))

#Verifica Estudantes

if menuPrincipal == 1:
        print("A opção escolhida foi: Opção 1. Estudantes. Escolha o que deseja fazer em seguida: 1. Incluir 2. Listar 3. Atualizar 4. Exluir 5. Voltar ao menu principal")

        escolhaEstudantes = int(input("Escolha uma opção:"))

        if escolhaEstudantes == 1:
            print("Você escolheu a opção 1: Incluir")
        elif escolhaEstudantes == 2:
                print("Você escolheu a opção 2: Listar")
        elif escolhaEstudantes == 3:
                print("Você escolheu a opção 3: Atualizar")
        elif escolhaEstudantes == 4:
                print("Você escolheu a opção 2: Excluir")
        elif escolhaEstudantes == 5:
                print("Voltando ao menu principal...")
        else:
            print("Opção inválida.")

    # Verifica Disciplinas

if menuPrincipal == 2:
        print("A opção escolhida foi: Disciplinas. Escolha o que deseja fazer em seguida: 1. Incluir 2. Listar 3. Atualizar 4. Exluir 5. Voltar ao menu principal")

        escolhaDisciplinas = int(input("Escolha uma opção:"))

        if escolhaDisciplinas == 1:
            print("Você escolheu a opção 1: Incluir")
        elif escolhaDisciplinas == 2:
            print("Você escolheu a opção 2: Listar")
        elif escolhaDisciplinas == 3:
            print("Você escolheu a opção 3: Atualizar")
        elif escolhaDisciplinas == 4:
            print("Você escolheu a opção 2: Excluir")
        elif escolhaDisciplinas == 5:
            print("Voltando ao menu principal...")
        else:
            print("Opção inválida.")

#Verifica Professores

if menuPrincipal == 3:
        print("A opção escolhida foi: Professores. Escolha o que deseja fazer em seguida: 1. Incluir 2. Listar 3. Atualizar 4. Exluir 5. Voltar ao menu principal")

        escolhaProfessores = int(input("Escolha uma opção:"))

        if escolhaProfessores == 1:
            print("Você escolheu a opção 1: Incluir")
        elif escolhaProfessores == 2:
            print("Você escolheu a opção 2: Listar")
        elif escolhaProfessores == 3:
            print("Você escolheu a opção 3: Atualizar")
        elif escolhaProfessores == 4:
            print("Você escolheu a opção 2: Excluir")
        elif escolhaProfessores == 5:
            print("Voltando ao menu principal...")
        else:
            print("Opção inválida.")

#Verifica Turmas

if menuPrincipal == 4:
        print("A opção escolhida foi: Turmas. Escolha o que deseja fazer em seguida: 1. Incluir 2. Listar 3. Atualizar 4. Exluir 5. Voltar ao menu principal")

        escolhaTurmas = int(input("Escolha uma opção:"))

        if escolhaTurmas == 1:
            print("Você escolheu a opção 1: Incluir")
        elif escolhaTurmas == 2:
            print("Você escolheu a opção 2: Listar")
        elif escolhaTurmas == 3:
            print("Você escolheu a opção 3: Atualizar")
        elif escolhaTurmas == 4:
            print("Você escolheu a opção 2: Excluir")
        elif escolhaTurmas == 5:
            print("Voltando ao menu principal...")
        else:
            print("Opção inválida.")

#Verifica Matrículas

if menuPrincipal == 5:
        print("A opção escolhida foi: Matrículas. Escolha o que deseja fazer em seguida: 1. Incluir 2. Listar 3. Atualizar 4. Exluir 5. Voltar ao menu principal")

        escolhaMatriculas = int(input("Escolha uma opção:"))

        if escolhaMatriculas == 1:
            print("Você escolheu a opção 1: Incluir")
        elif escolhaMatriculas == 2:
            print("Você escolheu a opção 2: Listar")
        elif escolhaMatriculas == 3:
            print("Você escolheu a opção 3: Atualizar")
        elif escolhaMatriculas == 4:
            print("Você escolheu a opção 2: Excluir")
        elif escolhaMatriculas == 5:
            print("Voltando ao menu principal...")
        else:
            print("Opção inválida.")

print("Fim da aplicação.")

