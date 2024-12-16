class Professor:
    def __init__(self, matricula, nome, sobrenome, idade, especialidade ):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.especialidade = especialidade
    
    def apresentarprofessor(self):
        print(f"Minha matrícula é: {self.matricula}, meu nome é: {self.nome} {self.sobrenome}, eu tenho: {self.idade} anos, e sou especialista em: {self.especialidade}.")


class Estudante:
    def __init__(self, matricula, nome, sobrenome, idade):
        self.matricula = matricula
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
    def apresentaraluno(self):
        print(f"Minha matrícula é: {self.matricula}, meu nome é: {self.nome} {self.sobrenome}, eu tenho: {self.idade} anos.")

professores = []
alunos = []

while True:
    print("menu\n 1 - cadastrar estudante\n 2 - cadastrar professor\n 3 - listar estudante\n 4 - listar professor\n 5 - alterar estudante pela matricula\n 6 - alterar estudante pelo nome\n 7 - alterar professor pela matricula\n 8 - alterar professor pelo nome\n 9 - excluir estudante pela matricula\n 10 - excluir professor pela matricula\n 0 - sair  ")

    opcao = int(input("Escolha uma opção do menu: "))
    

    if opcao == 1:
        matricula = int(input("digite sua matricula: "))
        nome = str(input("escreva seu nome: "))
        sobrenome = str(input("escreva seu sobrenome: "))
        idade =  int(input("digite sua idade: "))

        aluno = Estudante(matricula, nome, sobrenome, idade)
        alunos.append(aluno)
    

    if opcao == 2:
        matricula = int(input("digite sua matricula: "))
        nome = str(input("escreva seu nome: "))
        sobrenome = str(input("escreva seu sobrenome: "))
        idade =  int(input("digite sua idade:"))
        especialidade = str(input("escreva sua especialidade: "))

        prof = Professor(matricula, nome, sobrenome, idade, especialidade)
        professores.append(prof)
        
    
    if opcao == 3: 
        for aluno in alunos:
            aluno.apresentaraluno()
            
    
    if opcao == 4:
        for prof in professores:
            prof.apresentarprofessor()
            

    if opcao == 5:
        matricula_alterar = int(input("digite a matricula que deseja alterar: "))
        for aluno in alunos:
            if aluno.matricula == matricula_alterar:
                aluno.nome = str(input("escreva seu nome: "))
                aluno.sobrenome = str(input("escreva seu sobrenome: "))
                aluno.idade = int(input("escreva sua idade: "))
                print("informações alteradas com sucesso!")
                break
        else:
            print("aluno não encontrado!")


    if opcao == 6:      
        nome_alterar = str(input("escreva o nome do aluno que deseja alterar: "))
        for aluno in alunos:
            if aluno.nome == nome_alterar:
                aluno.matricula = int(input("digite sua matricula: "))
                aluno.sobrenome = str(input("escreva seu sobrenome: "))
                aluno.idade = int(input("digite a sua idade: "))
                print("informações alteradas com sucesso!")
                break
        else:
            print("aluno não encontrado.")
    

    if opcao == 7:
        professor_matricula = int(input("escreva a matricula do professor que deseja alterar: "))
        for prof in professores:
            if prof.matricula == professor_matricula:
                prof.nome = str(input("escreva seu nome: "))
                prof.sobrenome = str(input("escreva seu sobrenome: "))
                prof.idade = int(input("digite sua idade: "))
                prof.especialidade =  str(input("escreva sua especialidade: "))
                print("informações alteradas com sucesso!")
                break
        else:
            print("professor não encontrado.")
    

    if opcao == 8:
        professor_nome = str(input("escreva o nome do professor que deseja alterar: "))
        for prof in professores:
            if prof.nome == professor_nome:
                prof.matricula = int(input("escreva sua matricula: "))
                prof.sobrenome = str(input("escreva seu sobrenome: "))
                prof.idade = int(input("escreva sua idade: "))
                prof.especialidade = str(input("escreva sua especialidade: "))
                print("informações alteradas com sucesso!")
        else:
            print("professor não encontrado.")
    

    if opcao == 9:
        excluir_aluno = str(input("escreva a matricula do aluno que deseja excluir: "))
        for aluno in alunos:
            if aluno.matricula == excluir_aluno:
                alunos.remove(aluno)
                print("aluno removido com sucesso!")
                break
        else:
            print("aluno não encontrado.")
    

    if opcao == 10:
        excluir_prof =  str(input("escreva a matricula do professor que deseja excluir: "))
        for prof in professores:
            if prof.matricula == excluir_prof:
                professores.remove(prof)
                print("professor excluido com sucesso!")
                break
        else:
            print("professor não encotrado.")
    

    if opcao == 0:
        print("saindo...")
        break


        


