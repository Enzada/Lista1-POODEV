class ContaBancaria():
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Deposito de R${valor} realizado com sucesso.')
        else:
            print('Transacao invalida.')

    def sacar(self, valor):
        if self.saldo > 0 and self.saldo >= valor:
            self.saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso.')
        else:
            print('Valor de saque invalido.')

       
    def consultarSaldo(self):
        print(f'O saldo atual e: R${self.saldo}.')

conta = ContaBancaria(1000)
conta.depositar(500)
conta.sacar(350)
conta.consultarSaldo()