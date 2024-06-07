import datetime

class Banco:
    def __init__(self):
        self.usuarios = {}

    def cadastrar_nome(self, nome):
        self.usuarios[nome] = 0.0
        print("Nome cadastrado com sucesso!")

    def deletar_nome(self, nome):
        del self.usuarios[nome]
        print("Nome deletado com sucesso!")

    def entrar(self, nome):
        if nome in self.usuarios:
            while True:
                print("\nBem-vindo, {}!".format(nome))
                print("Escolha uma opção:")
                print("1. Consultar saldo")
                print("2. Depositar")
                print("3. Sacar")
                print("4. Sair do programa")
                opcao = input("Opção: ")

                if opcao == "1":
                    self.consultar_saldo(nome)
                elif opcao == "2":
                    valor = float(input("Digite o valor a depositar: "))
                    self.depositar(nome, valor)
                elif opcao == "3":
                    valor = float(input("Digite o valor a sacar: "))
                    self.sacar(nome, valor)
                elif opcao == "4":
                    print("Saindo do programa...")
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        else:
            print("Você precisa cadastrar seu nome antes de entrar no aplicativo.")

    def consultar_saldo(self, nome):
        saldo = self.usuarios[nome]
        data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("Seu saldo é R$ {:.2f} na data {}.".format(saldo, data_atual))

    def depositar(self, nome, valor):
        self.usuarios[nome] += valor
        print("Depósito realizado com sucesso!")

    def sacar(self, nome, valor):
        if valor <= self.usuarios[nome]:
            self.usuarios[nome] -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente!")

# Exemplo de uso:
banco = Banco()

while True:
    print("\nBem-vindo ao Banco!")
    print("Escolha uma opção:")
    print("1. Cadastrar nome")
    print("2. Deletar nome")
    print("3. Entrar")
    print("4. Sair do programa")
    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Digite seu nome: ")
        banco.cadastrar_nome(nome)
    elif opcao == "2":
        nome = input("Digite seu nome: ")
        banco.deletar_nome(nome)
    elif opcao == "3":
        nome = input("Digite seu nome: ")
        banco.entrar(nome)
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        break
