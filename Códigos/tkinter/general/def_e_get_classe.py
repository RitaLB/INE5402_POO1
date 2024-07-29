class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    #criando função de set possibilita que o dado nome e idade seja modificado por fora caso
    #antes tenha sido definido ocmo atributo privado. 
    def setNome(self, nome):
        self.nome = nome
    
    def setIdade(self, idade):
        self.idade = idade
    #criando função de get possibilita que o dado nome e idade seja consultado por fora caso
    #antes tenha sido definido ocmo atributo privado.
    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade