class Animal:  
    def __init__(self, nome, idade):  
        self.nome = nome  
        self.idade = idade  

    def emitir_som(self):  
        return "Som genérico de animal"  

class Cachorro(Animal):  # Definição da classe Cachorro, que herda da classe Animal
    def emitir_som(self):  # Sobrescrita do método emitir_som para um comportamento específico de Cachorro
        return "Latido"  # Retorna o som característico do cachorro

class Gato(Animal):  # Definição da classe Gato, que herda da classe Animal
    def emitir_som(self):  # Sobrescrita do método emitir_som para um comportamento específico de Gato
        return "Miau"  # Retorna o som característico do gato
