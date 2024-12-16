class Livro:
    def __init__(self, titulo, autor):
        self.titulo=titulo
        self.autor=autor
    
    def descricao(self):
        return f"{self.titulo} foi escrito por {self.autor}."
    
livro1 = Livro ("Dom quixote","Miguel De Cervantes")
print(livro1.descricao())


  