class Carro:
    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def pintar (self, novacor):
        self.cor = novacor 

    def mostrarcor(self):
        return f"a cor atual do carro é {self.cor}"
    
meucarro = Carro("fiat", "vermelho")

print(meucarro.mostrarcor())

meucarro.pintar("azul")
print(meucarro.mostrarcor())

