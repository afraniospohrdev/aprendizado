def adicionar_produto(inventario, nome, preco, quantidade):
    if nome in inventario:
        return inventario
    else:
        inventario[nome] = {"preco": preco, "quantidade": quantidade}
        return inventario

def listar_produtos(inventario):
    if not inventario:
        return []
    else:
        lista_produtos = []
        for produto, detalhes in sorted(inventario.items(), key=lambda x: x[0]):
            lista_produtos.append(f"{produto} - R${detalhes['preco']:.2f} - Qtd: {detalhes['quantidade']}")
        return lista_produtos

def remover_produto(inventario, nome):
    if nome in inventario:
        del inventario[nome]
        return inventario
    else:
        return inventario

def atualizar_quantidade(inventario, nome, quantidade):
    if nome in inventario:
        inventario[nome]["quantidade"] = quantidade
        return inventario
    else:
        return inventario

def exibir_menu():
    return (
        "1. Adicionar produto",
        "2. Listar produtos",
        "3. Remover produto",
        "4. Atualizar quantidade",
        "5. Sair do programa"
    )

def main():
    inventario = {}
    while True:
        print(*exibir_menu(), sep="\n")
        opcao = input("Escolha uma op o: ").strip()

        if opcao == "1":
            nome = input("Digite o nome do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            preco = float(input("Digite o preco do produto: "))
            adicionar_produto(inventario, nome, preco, quantidade)
        elif opcao == "2":
            print(*listar_produtos(inventario), sep="\n")
        elif opcao == "3":
            nome = input("Digite o nome do produto: ")
            remover_produto(inventario, nome)
        elif opcao == "4":
            nome = input("Digite o nome do produto: ")
            nova_qtd = int(input("Digite a nova quantidade do produto: "))
            atualizar_quantidade(inventario, nome, nova_qtd)
        elif opcao == "5":
            print("Saindo do programa...")
            break
   