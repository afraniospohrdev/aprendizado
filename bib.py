def obter_dados_livro(titulo, autor, quantidade):
    string_final = f"{titulo} {autor} {quantidade}"
    return string_final

def obter_quantidade_livro(entrada):
    if isinstance(entrada, dict) and "quantidade" in entrada:
        return entrada["quantidade"]
    elif isinstance(entrada, (int, float)):
        return entrada
    elif isinstance(entrada, str):
        try:
            return int(entrada)
        except ValueError:
            return 'Por favor, insira um número válido para a quantidade.'
    else:
        return None

def validar_livro_existe(biblioteca, titulo):
    if titulo in biblioteca:
        return True
    else:
        return f"Erro: O livro '{titulo}' não foi encontrado."

def adicionar_livro(biblioteca, titulo, autor, quantidade):
    if titulo in biblioteca:
        return "Livro já cadastrado"
    else:
        return f"Livro '{titulo}' adicionado com sucesso"
    

def listar_livros(biblioteca):
    if not biblioteca:
        return "Não há livros cadastrados."
    livros = []
    for titulo, dados in sorted(biblioteca.items()):
        livros.append(titulo)
    return livros

def remover_livro(biblioteca, titulo):
    if titulo in biblioteca:
        del biblioteca[titulo]
        return f"Livro '{titulo}' removido com sucesso!"
    else:
        return "Livro não encontrado."

def atualizar_quantidade(biblioteca, livro, nova_quantidade):
    if livro in biblioteca:
        while True:
            try:
                nova_quantidade = nova_quantidade
                break
            except ValueError:
                return "Entrada inválida. Por favor, digite um número inteiro."

        biblioteca[livro]["quantidade"] = nova_quantidade
        return f"Quantidade de exemplares do livro '{livro}' atualizada para {nova_quantidade}"
    else:
        return "Livro não encontrado."

def registrar_emprestimo(biblioteca, emprestimos,titulo, quantidade):
    if titulo in biblioteca:
        quantidade_atual = obter_quantidade_livro(biblioteca[titulo])

        if quantidade_atual >= quantidade:
            nova_quantidade = quantidade_atual - quantidade
            biblioteca[titulo]["quantidade"] = nova_quantidade
            emprestimos.append((titulo, quantidade))
            return f"{quantidade} exemplares de '{titulo}' emprestados com sucesso!"
        else:
            return "Não há exemplares disponíveis deste livro."
    else:
        return "Livro não encontrado."

def obter_quantidade_livro_para_emprestimo(biblioteca, titulo, quantidade):
    try:
        quantidade_atual = obter_quantidade_livro(biblioteca[titulo])
        if quantidade <= quantidade_atual:
            return quantidade
        elif quantidade > quantidade_atual:
            return quantidade_atual
    except (KeyError, ValueError):
        return 0

def exibir_historico_emprestimos(emprestimos):
    if not emprestimos:
        return "Não há histórico de empréstimos."
    return [f"{titulo}: {quantidade}" for titulo, quantidade in emprestimos]

def exibir_menu():
    """Exibe o menu de opcoes."""
    return """
    1. Adicionar livro
    2. Listar livros
    3. Remover livro
    4. Atualizar quantidade de livros
    5. Registrar emprestimo
    6. Exibir historico de emprestimos
    7. Sair
    """

    def main():
        biblioteca = {}
        emprestimos = []

        while True:
            print(exibir_menu())
            opcao = input("Escolha uma opcao: ")

            if opcao == "1":
                titulo = input("Titulo: ")
                autor = input("Autor: ")
                quantidade = int(input("Quantidade: "))
                adicionar_livro(biblioteca, titulo, autor, quantidade)
            elif opcao == "2":
                print(listar_livros(biblioteca))
            elif opcao == "3":
                titulo = input("Titulo: ")
                remover_livro(biblioteca, titulo)
            elif opcao == "4":
                titulo = input("Titulo: ")
                quantidade = int(input("Quantidade: "))
                atualizar_quantidade(biblioteca, titulo, quantidade)
            elif opcao == "5":
                titulo = input("Titulo: ")
                quantidade_emprestada = int(input("Quantidade a emprestar: "))
                quantidade_valida = obter_quantidade_livro_para_emprestimo(biblioteca, titulo, quantidade_emprestada)
                if quantidade_valida > 0:
                    registrar_emprestimo(biblioteca, titulo, quantidade_valida, emprestimos)
                else:
                    print(quantidade_valida)
            elif opcao == "6":
                print(exibir_historico_emprestimos(emprestimos))
            elif opcao == "7":
                print("Saindo do programa...")
                break
            else:
                print("Opcao invalida. Tente novamente.")
