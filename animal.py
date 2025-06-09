# Classe Animal (classe pai)
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("O animal emitiu um som genérico.")

# Classe Cachorro (classe filha herdando de Animal)
class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)  # Chama o construtor da classe pai (Animal)

    def emitir_som(self):
        print("O cachorro latiu!")

# Classe Gato (classe filha herdando de Animal)
class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)  # Chama o construtor da classe pai (Animal)

    def emitir_som(self):
        print("O gato miou!")

# Programa principal
if __name__ == "__main__":
    # Criação dos objetos
    cachorro = Cachorro("Quinho", 5)
    gato = Gato("Nina", 3)

    # Chamada dos métodos
    print(f"Nome do cachorro: {cachorro.nome}, idade: {cachorro.idade}")
    cachorro.emitir_som()

    print(f"\nNome do gato: {gato.nome}, idade: {gato.idade}")
    gato.emitir_som()

      