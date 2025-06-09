def calculadora():
    # Função para obter um número válido do usuário
    def obter_numero(mensagem):
        while True:
            try:
                valor = float(input(mensagem))
                return valor
            except ValueError:
                print("Entrada inválida. Por favor, insira um número.")

    # Solicitar os números ao usuário
    numero1 = obter_numero("Insira o primeiro número: ")
    numero2 = obter_numero("Insira o segundo número: ")

    # Função para exibir o menu e obter a escolha do usuário
    def exibir_menu():
        opcoes = [
            "Soma",
            "Subtração",
            "Multiplicação",
            "Divisão"
        ]
        print("\nEscolha uma operação:")
        for i, op in enumerate(opcoes, 1):
            print(f"{i}. {op}")
        while True:
            try:
                escolha = int(input("Digite o número da operação: "))
                if 1 <= escolha <= len(opcoes):
                    return escolha - 1  # Ajuste para índices 0-base
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número.")

    # Definir funções anônimas (lambdas) para cada operação
    operacoes = {
        0: lambda x, y: x + y,
        1: lambda x, y: x - y,
        2: lambda x, y: x * y,
        3: lambda x, y: x / y if y != 0 else None
    }

    # Loop principal para realizar cálculos repetidamente
    while True:
        # Exibir o menu e obter a escolha do usuário
        escolha = exibir_menu()

        # Escolher a operação e realizar o cálculo
        operacao = operacoes.get(escolha)
        if operacao:
            if escolha == 3 and numero2 == 0:
                print("Divisão por zero não é permitida.")
                numero2 = obter_numero("Insira um novo valor para o segundo número: ")
                operacao = operacoes.get(escolha)  # Atualizar a operação com o novo valor
                if operacao:
                    resultado = operacao(numero1, numero2)
                    print(f"Resultado: {resultado}")
                else:
                    print("Erro na operação.")
            else:
                resultado = operacao(numero1, numero2)
                print(f"Resultado: {resultado}")
        else:
            print("Opção de operação inválida.")

        # Pergunta se o usuário quer realizar outra operação ou encerrar
        while True:
            continuar = input("\nDeseja realizar outra operação? (S/N): ").upper()
            if continuar == "S":
                break  # Volta ao loop principal
            elif continuar == "N":
                print("Encerrando a calculadora...")
                return  # Encerra o programa
            else:
                print("Opção inválida. Digite 'S' para continuar ou 'N' para encerrar.")

# Iniciar a calculadora
if __name__ == "__main__":
    calculadora()