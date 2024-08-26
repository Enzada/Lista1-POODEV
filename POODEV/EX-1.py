class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def registro(self):
        print(f'O nome da pessoa e {self.nome} e sua idade e {self.idade}')

pessoa1 = Pessoa('Carlos', 45)
pessoa2 = Pessoa('Amanda', 23)

pessoa1.registro()
pessoa2.registro()
