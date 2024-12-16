

class Pessoa:
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
    
    def imc(self):
        return self.peso/(self.altura ** 2)

    def caracteristicas(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}, Altura: {self.altura} m, Peso: {self.peso} kg, {self.imc():.2f}")

cadastro=[]

while True:
    print(" MENU\n 1 - cadastrar\n 2 - listar\n 3 - exluir\n 4 - alterar\n 0 - sair")

    opcao=int(input("digite o valor de uma opção do menu: "))
    
    if opcao == 1:
        nome=input("escreva o seu nome: ")
        idade=int(input("digite a sua idade: "))
        altura = float(input("escreva a sua altura: "))
        peso = float(input("digite o seu peso: "))

        individuo= Pessoa(nome, idade, altura, peso)
        cadastro.append(individuo)
        print("cadastro realizado com sucesso!")

    if opcao == 2:
        if len (cadastro) == 0:
            print("Não há pessoa cadastradas!")
        else:
            for individuo in cadastro:
                individuo.caracteristicas()
                break
            
    if opcao == 3:
        y=str(input("escreva o nome da pessoa que deseja excluir: "))
        for individuo in cadastro:
            if individuo.nome == y:
                cadastro.remove(individuo)
                print("pessoa removida com sucesso!")
                break
            else:
                print("Essa pessoa não está cadastrada.")
    
    if opcao == 4:
        x= str(input("escreva o nome da pessoa que deseja alterar as informações: "))
        for indivivuo in cadastro:
            if individuo.nome == x:
                individuo.idade = int(input("escreva a nova idade: "))
                individuo.altura = float(input("escreva a nova altura: "))
                individuo.peso = float(input("escreva o novo peso: "))
                print("informações alteradas com sucesso!")
                break
            else: 
                print("pessoa não cadastrada!")
        
        
    if opcao == 0:
        print("saindo do programa...")   
        break