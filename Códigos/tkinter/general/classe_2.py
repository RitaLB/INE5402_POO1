#classe:
class controleremoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
#função:      
def novocontrole():
    cor, altura, profundidade, largura = input().split()
    return controleremoto(cor, altura, profundidade, largura)

controle1 = novocontrole()

print(controle1.cor)