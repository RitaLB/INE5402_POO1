class Batata():

    def __init__(self,tipo: str, gramas: int):

        self.tipo = tipo
        self.gramas = gramas
        self.x = "coisa"

    def reduzir_batat(self,qtd_reduzir):
        self.gramas -= qtd_reduzir

        x = "pastel"

    def mudar_x(self):
        x= "mudado"
    

    def __str__(self):
        Batata_em_string = str(self.tipo) + "\n"+ str(self.gramas) + "\n" + str(self.x) 
        return Batata_em_string

# apenas se batatinhas for o arquivo rodado, o if vai ser executado:
if __name__ == "__main__":
    batata = Batata("doce",234)
    print(batata)