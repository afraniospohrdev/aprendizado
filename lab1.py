# Lista de convidados VIP (pode ser modificada nos testes)
convidados_vip = ["Alice", "Bob", "Carol"]

# Função para verificar se a idade permite entrada
def verificar_idade(idade):
    if idade >= 18:
        return "Entrada permitida. Bem-vindo ao evento!"
    else:
        return "Entrada negada. Este evento é apenas para maiores de idade."

# Função para verificar se o nome está na lista VIP
def verificar_vip(nome):
    if nome in convidados_vip:
        return "Você é um convidado VIP! Aproveite o evento com acesso especial."
    else:
        return "Entrada negada."

# Programa principal
def main():
    while True:
        try:
            idade = int (input("Informe a sua idade: "))
        except ValueError:
            print("A idade deve ser um numero inteiro")
            continue

        if verificar_idade(idade) == "Entrada permitida":
            nome = input("Informe seu nome: ")
            if not nome:
                break
            if verificar_vip(nome) == "Entrada VIP":
                print(f"Bem-vindo(a), {nome}!")
            else:
                print("Entrada padrão")
        else:
            print("Entrada negada")

if __name__ == "____":
    ____()