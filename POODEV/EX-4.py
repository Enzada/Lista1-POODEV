class Calculadora():
    def __init__(self,inicial):
        self.inicial = inicial
    
    def somar(self,valor):
        self.inicial += valor

    def subtrair(self, valor):
        self.inicial -= valor
    
    def multiplicar(self,valor):
        self.inicial *= valor

    def dividir(self,valor):
        if valor == 0:
            print('Erro: Divisão por 0')
            return None
        else:
            self.inicial /= valor
    

    def mostra_conta(self):
        print(f'O resultado é: {self.inicial}')


conta = Calculadora(9)
conta.somar(3)
conta.subtrair(20)
conta.multiplicar(2)
conta.dividir(4)
conta.mostra_conta()