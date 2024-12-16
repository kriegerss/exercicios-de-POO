while True:
    class Conta_bancaria:
        def __init__(self, titular, saldo):
            self.titular = titular
            self.saldo = saldo


    def sacar():
        valor_conta=int(input("escreva o saldo atual da sua conta: "))
        saque=int(input("escreva o valor que deseja sacar: "))
        return (valor_conta - saque)

    print("O saldo atual da sua conta é: ", sacar())
    print("")

