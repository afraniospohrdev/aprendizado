def adicionar_produto(estoque):
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade inicial: "))
    estoque[nome] = quantidade
    print(f"Produto '{nome}' adicionado com sucesso.")

def listar_produtos(estoque):
    if not estoque:
        print("O estoque está vazio.")
        return
    print("Produtos em estoque:")
    for nome, quantidade in estoque.items():
        print(f"- {nome}: {quantidade}")

def remover_produto(estoque):
    nome = input("Nome do produto a remover: ")
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido com sucesso.")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

def atualizar_quantidade(estoque):
    nome = input("Nome do produto a atualizar: ")
    if nome in estoque:
        nova_quantidade = int(input(f"Nova quantidade de {nome}: "))
        estoque[nome] = nova_quantidade
        print(f"Quantidade de '{nome}' atualizada com sucesso.")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

def main():
    estoque = {}
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Remover produto")
        print("4. Atualizar quantidade")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            listar_produtos(estoque)
        elif opcao == "3":
            remover_produto(estoque)
        elif opcao == "4":
            atualizar_quantidade(estoque)
        elif opcao == "5":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()