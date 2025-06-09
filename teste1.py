e# Classe para representar um produto
class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"Nome: {self.nome}, Quantidade: {self.quantidade}, Preço: {self.preco}"

# Lista para armazenar os produtos
estoque = []

# Funções para as operações de gestão de estoque

def adicionar_produto(estoque):
    """Adiciona um novo produto ao estoque."""
    nome = input("Digite o nome do produto: ")
    try:
        quantidade = int(input("Digite a quantidade do produto: "))
    except ValueError:
        print("Quantidade inválida. Digite um número inteiro.")
        return
    try:
        preco = float(input("Digite o preço do produto: "))
    except ValueError:
        print("Preço inválido. Digite um número decimal.")
        return

    novo_produto = Produto(nome, quantidade, preco)
    estoque.append(novo_produto)
    print(f"Produto '{nome}' adicionado ao estoque.")

def listar_produtos(estoque):
    """Lista todos os produtos no estoque."""
    if not estoque:
        print("O estoque está vazio.")
        return

    print("\nLista de produtos no estoque:")
    for produto in estoque:
        print(produto)

def remover_produto(estoque):
    """Remove um produto do estoque."""
    nome_remover = input("Digite o nome do produto a ser removido: ")
    for produto in estoque:
        if produto.nome.lower() == nome_remover.lower():
            estoque.remove(produto)
            print(f"Produto '{nome_remover}' removido com sucesso.")
            return
    print(f"Produto '{nome_remover}' não encontrado no estoque.")

def atualizar_quantidade(estoque):
    """Atualiza a quantidade de um produto no estoque."""
    nome_atualizar = input("Digite o nome do produto a ser atualizado: ")
    for produto in estoque:
        if produto.nome.lower() == nome_atualizar.lower():
            try:
                nova_quantidade = int(input("Digite a nova quantidade do produto: "))
            except ValueError:
                print("Quantidade inválida. Digite um número inteiro.")
                return
            produto.quantidade = nova_quantidade
            print(f"Estoque do produto '{nome_atualizar}' atualizado para {nova_quantidade}.")
            return
    print(f"Produto '{nome_atualizar}' não encontrado no estoque.")

# Menu interativo
def exibir_menu():
    """Exibe o menu e solicita a escolha do usuário."""
    while True:
        print("\n--- Menu de Gestão de Estoque ---")
        print("1. Adicionar Produto")
        print("2. Listar Produtos")
        print("3. Remover Produto")
        print("4. Atualizar Estoque")
        print("5. Sair")

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
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Inicia o programa
if __name__ == "__main__":
    exibir_menu()
