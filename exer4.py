class Produto:
    def __init__(self, nome, quantidade):
      
        self.nome = nome
        self.quantidade = quantidade

    def esta_disponivel(self):
      
        return self.quantidade > 0

    def vender(self):
        
        if self.esta_disponivel():
            self.quantidade -= 1
            print(f"Produto '{self.nome}' vendido! Quantidade restante: {self.quantidade}")
        else:
            print(f"Produto '{self.nome}' não está disponível para venda!")


produto1 = Produto("Caneta", 3)  

disponivel = produto1.esta_disponivel()
print(f"Produto '{produto1.nome}' está disponível? {disponivel}")

for i in range (3):
    produto1.vender()

disponivel = produto1.esta_disponivel()
print(f"Produto '{produto1.nome}' está disponível? {disponivel}")