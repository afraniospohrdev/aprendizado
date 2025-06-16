# Criar uma estrutura para armazenar os livros (dicionário de dicionários)
biblioteca = {}

# Definir o menu de opções da biblioteca
def exibir_menu():
    print("\n--- Menu da Biblioteca ---")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Remover livro")
    print("4. Atualizar quantidade de livros")
    print("5. Registrar empréstimo")
    print("6. Exibir histórico de empréstimos")
    print("7. Sair")

# Função para adicionar um livro à biblioteca
def adicionar_livro():
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor: ")
    quantidade = int(input("Digite a quantidade de exemplares: "))

    # Verificar se o livro já existe
    if titulo in biblioteca:
        print("Livro já cadastrado.")
        return

    # Criar um dicionário para armazenar os dados do livro
    livro = {"autor": autor, "quantidade": quantidade}
    biblioteca[titulo] = livro
    print(f"Livro '{titulo}' adicionado com sucesso!")

# Função para listar todos os livros
def listar_livros():
    """Exibe todos os livros da biblioteca."""
    if not biblioteca:
        print("A biblioteca está vazia.")
        return

    print("\n--- Lista de Livros ---")
    for titulo, dados in sorted(biblioteca.items()):
        print(f"Título: {titulo}")
        print(f"Autor: {dados['autor']}")
        print(f"Quantidade: {dados['quantidade']}")
        print("---")

# Função para remover um livro da biblioteca
def remover_livro():
    titulo = input("Digite o título do livro a ser removido: ")

    if titulo in biblioteca:
        del biblioteca[titulo]
        print(f"Livro '{titulo}' removido com sucesso!")
    else:
        print("Livro não encontrado.")

# Função para atualizar a quantidade de livros
def atualizar_quantidade():
    titulo = input("Digite o título do livro a ser atualizado: ")

    if titulo in biblioteca:
        nova_quantidade = int(input("Digite a nova quantidade: "))
        biblioteca[titulo]["quantidade"] = nova_quantidade
        print(f"Quantidade do livro '{titulo}' atualizada com sucesso!")
    else:
        print("Livro não encontrado.")

# Função para registrar um empréstimo
def registrar_emprestimo():
    """Registra um empréstimo de um livro."""
    titulo = input("Digite o título do livro a ser emprestado: ")

    if titulo in biblioteca:
        quantidade_atual = biblioteca[titulo]["quantidade"]
        if quantidade_atual > 0:
            biblioteca[titulo]["quantidade"] = quantidade_atual - 1
            print(f"Livro '{titulo}' emprestado com sucesso!")
        else:
            print("Não há exemplares disponíveis deste livro.")
    else:
        print("Livro não encontrado.")

# Função para exibir o histórico de empréstimos
def exibir_historico():
    # (Implementar o histórico de empréstimos, que pode ser feito com uma lista)
    print("Histórico de Empréstimos:")
    for titulo, quantidade in exibir_historico.items():
        print(f"- {titulo}: {quantidade} emprestados")

# Loop principal do programa
while True:
    exibir_menu()

    opcao = input("Escolha uma opção (1-7): ")

    if opcao == "1":
        adicionar_livro()
    elif opcao == "2":
        listar_livros()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        atualizar_quantidade()
    elif opcao == "5":
        registrar_emprestimo()
    elif opcao == "6":
        exibir_historico()
    elif opcao == "7":
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")