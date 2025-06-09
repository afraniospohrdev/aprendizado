# Variável global de tarefas
tarefas = {}

def adicionar_tarefa(nome):
    if nome in tarefas:
        return ("Essa tarefa já existe.")
    else:
        tarefas[nome] = False
        return (f"Tarefa '{nome}' adicionada com sucesso!!")

def listar_tarefas(tarefas):
    if not tarefas:
        return ("Nenhuma tarefa cadastrada.")
    else:
        resultado = ["Lista de tarefas"]
        for nome, concluída in sorted(tarefas.items(), key=lambda item: item[0]):
            status = "✅ Concluida" if concluida else "❌ Nao concluida"
            resultado.append(f"{nome}: {status}")
        return "\n".join(resultado)


def remover_tarefa(nome):
    if nome in tarefas:
        del tarefas[nome]
        return (f"Tarefa '{nome}' removida com sucesso!")
    else:
        return ("Erro: Tarefa não encontrada.")

def marcar_concluida(nome):
    if nome in tarefas:
        tarefas[nome] = True
        return (f"Tarefa '{nome}' marcada como concluída!")
    else:
	    return (f"Erro: Tarefa não encontrada.")

def exibir_menu():
    return (
	    "\n1 - Adicionar tarefa"
	    "\n2 - Listar tarefas"
	    "\n3 - Remover Tarefa"
	    "\n4 - Marcar tarefa como concluída"
	    "\n5 - Sair"
    )

def main():
    while True:
        print(exibir_menu())
        opcao = input("Digite a opção desejada ").lower()

        if opcao == "1":
            nome = input("Digite o nome da tarefa: ")
            print(adicionar_tarefa(tarefas,nome))
        elif opcao == "2":
            print(listar_tarefas(tarefas))
        elif opcao == "3":
            nome = input("Digite o nome da tarefa que quer remover ")
            print(remover_tarefa(tarefas,nome))
        elif opcao == "4":
            nome = input("Digite o nome da tarefa que quer concluir ")
            print(marcar_concluida(tarefas,nome))
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida")


