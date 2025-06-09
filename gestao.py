def menu():
    """Exibe o menu de opções."""
    print("\n-- Gerenciamento de Estoque --")
    print("1. Adicionar produto")
    print("2. Listar produtos")
    print("3. Remover produto")
    print("4. Atualizar quantidade de produto")
    print("5. Sair")

def adicionar_produto(estoque):
    """Adiciona um novo produto ao estoque."""
    nome = input("Nome do produto: ")
    if nome in estoque:
        print("Produto já cadastrado.")
        return
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: "))
    estoque[nome] = {"quantidade": quantidade, "preço": preco}
    print("Produto adicionado com sucesso!")

def listar_produtos(estoque):
    """Lista todos os produtos no estoque."""
    if not estoque:
        print("O estoque está vazio.")
        return
    print("\n-- Lista de Produtos --")
    for nome, detalhes in estoque.items():
        print(f"- {nome}: Quantidade: {detalhes['quantidade']}, Preço: {detalhes['preço']:.2f}")

def remover_produto(estoque):
    """Remove um produto do estoque."""
    nome = input("Nome do produto a remover: ")
    if nome in estoque:
        del estoque[nome]
        print("Produto removido com sucesso!")
    else:
        print("Produto não encontrado.")

def atualizar_quantidade(estoque):
    """Atualiza a quantidade de um produto no estoque."""
    nome = input("Nome do produto a atualizar: ")
    if nome in estoque:
        nova_quantidade = int(input("Nova quantidade: "))
        estoque[nome]["quantidade"] = nova_quantidade
        print("Quantidade atualizada com sucesso!")
    else:
        print("Produto não encontrado.")

# Código principal
estoque = {}

while True:
    menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_produto(estoque)
    elif escolha == "2":
        listar_produtos(estoque)
    elif escolha == "3":
        remover_produto(estoque)
    elif escolha == "4":
        atualizar_quantidade(estoque)
    elif escolha == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")