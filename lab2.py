# Variável global de tarefas
tarefas = {}

def adicionar_tarefa(lista_tarefas):
    nova_tarefa = input("Digite a nova tarefa: ")
    lista_tarefas.append({"tarefa": nova_tarefa, "concluida": False})
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(lista_tarefas):
    if not lista_tarefas:
        print("A lista de tarefas está vazia.")
        return
    print("\nLista de Tarefas:")
    for i, tarefa in enumerate(lista_tarefas):
        status = "[X]" if tarefa["concluida"] else "[ ]"
        print(f"{i+1}. {status} {tarefa['tarefa']}")

def remover_tarefa(lista_tarefas):
    listar_tarefas(lista_tarefas)
    try:
        indice = int(input("Digite o número da tarefa a remover: ")) - 1
        if 0 <= indice < len(lista_tarefas):
            del lista_tarefas[indice]
            print("Tarefa removida com sucesso!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

def marcar_concluida(lista_tarefas):
    listar_tarefas(lista_tarefas)
    try:
        indice = int(input("Digite o número da tarefa a marcar como concluída: ")) - 1
        if 0 <= indice < len(lista_tarefas):
            lista_tarefas[indice]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

def main():
    lista_tarefas = []
    while True:
        print("\nGerenciador de Tarefas")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Remover Tarefa")
        print("4. Marcar como Concluída")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa(lista_tarefas)
        elif escolha == "2":
            listar_tarefas(lista_tarefas)
        elif escolha == "3":
            remover_tarefa(lista_tarefas)
        elif escolha == "4":
            marcar_concluida(lista_tarefas)
        elif escolha == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()