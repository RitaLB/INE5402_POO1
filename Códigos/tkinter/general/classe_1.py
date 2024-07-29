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
        
        
#criando vários controles com um vetor:
n = int(input())
controles = [None]*n
for i in range (n):
    controles[i]= novocontrole()
    
#dando nome aos controles com um dicionário:
meus_controles = {}
meus_controles['controle_1'] = controles[1]

# printando uma característica de um determinado controle:
print(meus_controles['controle_1'].cor)