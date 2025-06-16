# Dicionário para armazenar produtos
estoque = {}

def adicionar_produto(estoque):
    """Adiciona um novo produto ao estoque."""
    nome = input("Digite o nome do produto: ")
    if nome in estoque:
        print(f"Produto '{nome}' já existe no estoque.")
        return

    while True:
        try:
            preco = float(input("Digite o preço do produto: "))
            quantidade = int(input("Digite a quantidade em estoque: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira números válidos para o preço e a quantidade.")

    estoque[nome] = {"preço": preco, "quantidade": quantidade}
    print(f"Produto '{nome}' adicionado ao estoque.")

def listar_produtos(estoque):
    """Exibe todos os produtos disponíveis no estoque."""
    if not estoque:
        print("Não há produtos no estoque.")
        return

    print("\n--- Produtos Disponíveis ---")
    for produto, detalhes in sorted(estoque.items()):
        print(
            f"Produto: {produto}, Preço: R${detalhes['preço']:.2f}, "
            f"Quantidade em estoque: {detalhes['quantidade']}"
        )

def remover_produto(estoque, nome=None):
    """Remove um produto do estoque."""
    nome = nome or input("Digite o nome do produto a ser removido: ")

    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido do estoque.")
    else:
        print(f"Produto '{nome}' não encontrado.")

def atualizar_produto(estoque):
    """Atualiza informações de um produto no estoque."""
    nome = input("Digite o nome do produto a ser atualizado: ")
    if nome in estoque:
        print("\n--- Atualizar Produto ---")

        while True:
            try:
                novo_preço = input("Digite o novo preço (enter para manter): ")
                if not novo_preço:
                    novo_preço = estoque[nome]["preço"]
                else:
                    novo_preço = float(novo_preço)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

        while True:
            try:
                nova_quantidade = input("Digite a nova quantidade (enter para manter): ")
                if not nova_quantidade:
                    nova_quantidade = estoque[nome]["quantidade"]
                else:
                    nova_quantidade = int(nova_quantidade)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

        estoque[nome]["preço"] = novo_preço
        estoque[nome]["quantidade"] = nova_quantidade
        print(f"Produto '{nome}' atualizado.")
    else:
        print(f"Produto '{nome}' não encontrado.")

def menu():
    """Exibe o menu interativo e lida com as escolhas do usuário."""
    opcoes = {
        "1": adicionar_produto,
        "2": listar_produtos,
        "3": remover_produto,
        "4": atualizar_produto,
        "5": lambda: print("Saindo do programa...") or exit(0),
    }

    while True:
        print("\n--- Menu de Gestão de Estoque ---")
        for numero, descricao in opcoes.items():
            print(f"{numero}. {descricao.__name__.replace('_', ' ').capitalize()}")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha in opcoes:
            opcoes[escolha](estoque)
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
menu()